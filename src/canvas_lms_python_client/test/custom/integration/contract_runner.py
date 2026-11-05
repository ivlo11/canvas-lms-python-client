"""
Calls every GET operation through the generated client, as one role.

Used by the contract test and as the role probe for canvas-lms's
script/api_docs_audit. Everything it writes or reports holds operation names, key
names, JSON type names, status codes and error kinds: never response values or
tokens. It only sends GET requests.
"""

import asyncio
import importlib
import inspect
import json
import pathlib
import pkgutil
import re
from dataclasses import dataclass, field

import aiohttp
from pydantic import ValidationError

import canvas_lms_python_client.api
from canvas_lms_python_client.api_client import ApiClient
from canvas_lms_python_client.configuration import Configuration

# Routes that open sessions, mint tokens, download files or launch tools
SKIPPED_ROUTES = (
    ("session", re.compile(r"session|logout|login|authorize", re.I)),
    ("token", re.compile(r"token|jwks|public_jwk", re.I)),
    ("download", re.compile(r"download|export|/content$|public_url", re.I)),
    ("launch", re.compile(r"launch", re.I)),
)
SERIALIZED_REQUEST = re.compile(
    r"def _(\w+)_serialize\(.*?method='(\w+)',\s*resource_path='([^']+)'",
    re.S,
)
PATH_PARAMETER = re.compile(r"\{(\w+)\}")
KEY_NAME = re.compile(r"\A[A-Za-z_][A-Za-z0-9_-]{0,63}\Z")
LONG_HEX_RUN = re.compile(r"[0-9a-fA-F]{16}")
DYNAMIC_KEY = "*"
MAX_DEPTH = 8
MAX_ARRAY_ITEMS = 25
PER_PAGE = 10
REQUEST_TIMEOUT = 120
CONCURRENCY = 4
SEEDED_COURSE_ID = "2"

# Where to find an id when the path before a parameter isn't a list of them
PARAMETER_LISTS = {
    "assignment_id": "/api/v1/courses/{course_id}/assignments",
    "assignment_group_id": "/api/v1/courses/{course_id}/assignment_groups",
    "communication_channel_id": "/api/v1/users/self/communication_channels",
    "content_migration_id": "/api/v1/courses/{course_id}/content_migrations",
    "conversation_id": "/api/v1/conversations",
    "course_section_id": "/api/v1/courses/{course_id}/sections",
    "discussion_topic_id": "/api/v1/courses/{course_id}/discussion_topics",
    "enrollment_id": "/api/v1/courses/{course_id}/enrollments",
    "file_id": "/api/v1/courses/{course_id}/files",
    "folder_id": "/api/v1/courses/{course_id}/folders",
    "grading_period_id": "/api/v1/courses/{course_id}/grading_periods",
    "group_category_id": "/api/v1/courses/{course_id}/group_categories",
    "group_id": "/api/v1/courses/{course_id}/groups",
    "module_id": "/api/v1/courses/{course_id}/modules",
    "poll_id": "/api/v1/polls",
    "quiz_id": "/api/v1/courses/{course_id}/quizzes",
    "rubric_id": "/api/v1/courses/{course_id}/rubrics",
    "section_id": "/api/v1/courses/{course_id}/sections",
    "student_id": "/api/v1/courses/{course_id}/students",
    "term_id": "/api/v1/accounts/self/terms",
    "topic_id": "/api/v1/courses/{course_id}/discussion_topics",
}
SELF_PARAMETERS = {"account_id": "self", "user_id": "self"}
SLUG_PARAMETERS = {"date": "date", "feature": "feature", "report": "report", "url": "url", "url_or_id": "url"}
# Values for required query parameters that need no lookup
QUERY_VALUES = {"domain": "example.com", "ns": "seeded", "q": "seeded"}


@dataclass(frozen=True)
class Operation:
    """One GET operation of the generated client."""

    name: str
    module: str
    api_class: str
    route: str


@dataclass
class RoleResult:
    """What happened to every operation for one role."""

    role: str
    outcomes: dict = field(default_factory=dict)
    failures: dict = field(default_factory=dict)
    records: list = field(default_factory=list)

    def counts(self):
        """Count outcomes, grouping http_* and skipped:* together."""
        counts = {}
        for outcome in self.outcomes.values():
            group = outcome.split(":")[0]
            group = "http_error" if group.startswith("http_") else group
            counts[group] = counts.get(group, 0) + 1
        return counts


def discover_operations():
    """Return every GET operation in the generated API modules."""
    package = canvas_lms_python_client.api
    operations = []
    for module_info in pkgutil.iter_modules(package.__path__):
        name = f"{package.__name__}.{module_info.name}"
        module = importlib.import_module(name)
        classes = [c for c_name, c in inspect.getmembers(module, inspect.isclass) if c.__module__ == name]
        if not classes:
            continue
        source = inspect.getsource(module)
        for operation, method, route in SERIALIZED_REQUEST.findall(source):
            if method == "GET":
                operations.append(Operation(operation, name, classes[0].__name__, route))
    return sorted(operations, key=lambda item: item.name)


def skip_reason(route):
    """Return why a route must not be called, or None."""
    for reason, pattern in SKIPPED_ROUTES:
        if pattern.search(route):
            return reason
    return None


def key_name(key):
    """Keep a key's name, unless the key may itself be data."""
    text = str(key)
    return text if KEY_NAME.match(text) and not LONG_HEX_RUN.search(text) else DYNAMIC_KEY


def type_of(value):
    """JSON type name of a decoded value."""
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    return "null"


def container_of(body):
    """Whether a decoded body is a list, an object, a scalar or absent."""
    if body is None:
        return "none"
    if isinstance(body, list):
        return "list"
    return "object" if isinstance(body, dict) else "scalar"


def collect_fields(value, path, fields, depth=0):
    """Record key paths and type names, using [] for array items."""
    if depth > MAX_DEPTH:
        return
    if isinstance(value, dict):
        for key, item in value.items():
            name = key_name(key)
            item_path = f"{path}.{name}" if path else name
            fields.setdefault(item_path, set()).add(type_of(item))
            collect_fields(item, item_path, fields, depth + 1)
    elif isinstance(value, list):
        item_path = f"{path}[]"
        for item in value[:MAX_ARRAY_ITEMS]:
            fields.setdefault(item_path, set()).add(type_of(item))
            collect_fields(item, item_path, fields, depth + 1)


def build_record(route, status, role, body):
    """The evidence record for one response: names and types only."""
    fields = {}
    collect_fields(body, "", fields)
    return {
        "route": route,
        "method": "GET",
        "status": status,
        "role": role,
        "container": container_of(body),
        "api": True,
        "string_ids": False,
        "fields": {path: sorted(types) for path, types in fields.items()},
    }


def parse_error_kinds(error):
    """Where and how a response failed validation, without its input."""
    return sorted(
        {
            f"{'.'.join(str(part) for part in item['loc'])}:{item['type']}"
            for item in error.errors(include_input=False, include_url=False, include_context=False)
        }
    )


class ContractRunner:
    """Calls every GET operation as one role."""

    def __init__(self, base_url, token, role):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.role = role
        self.result = RoleResult(role)
        self._lists = {}
        self._apis = {}
        self._semaphore = asyncio.Semaphore(CONCURRENCY)
        self._session = None
        self._course_id = None

    async def run(self, operations):
        """Run all operations and return the role's result."""
        config = Configuration(host=self.base_url, access_token=self.token)
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}
        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
        async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session, ApiClient(config) as client:
            self._session = session
            self._course_id = await self._find_course()
            await asyncio.gather(*(self._call(operation, client) for operation in operations))
        return self.result

    async def _get_json(self, path):
        params = {"per_page": str(PER_PAGE)}
        async with self._session.get(f"{self.base_url}{path}", params=params) as response:
            if response.status != 200:
                return response.status, None
            text = await response.text()
        return 200, json.loads(text.removeprefix("while(1);"))

    async def _find_course(self):
        try:
            status, _ = await self._get_json(f"/api/v1/courses/{SEEDED_COURSE_ID}")
            if status == 200:
                return SEEDED_COURSE_ID
            _, courses = await self._get_json("/api/v1/courses")
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError):
            return None
        return str(courses[0]["id"]) if courses else None

    async def _first_value(self, path, attribute="id"):
        """The first item's attribute in a list, cached by path."""
        cached = self._lists.get((path, attribute))
        if cached is not None:
            return await cached

        async def fetch():
            try:
                status, body = await self._get_json(path)
            except (aiohttp.ClientError, asyncio.TimeoutError, ValueError):
                return None
            if status != 200:
                return None
            if isinstance(body, dict):
                lists = [value for value in body.values() if isinstance(value, list)]
                body = lists[0] if len(lists) == 1 else None
            if isinstance(body, list) and body and isinstance(body[0], dict):
                value = body[0].get(attribute)
                return None if value is None else str(value)
            return None

        task = asyncio.ensure_future(fetch())
        self._lists[(path, attribute)] = task
        return await task

    async def _resolve_path_values(self, route):
        """Find a value for each path parameter, or return the one that has none."""
        values = {}
        for match in PATH_PARAMETER.finditer(route):
            name = match.group(1)
            parent = route[: match.start()].rstrip("/")
            for known, value in values.items():
                parent = parent.replace(f"{{{known}}}", value)
            value = await self._value_for(name, parent)
            if value is None:
                return None, name
            values[name] = value
        return values, None

    async def _value_for(self, name, parent):
        if name == "course_id":
            return self._course_id
        if name in SELF_PARAMETERS:
            return SELF_PARAMETERS[name]
        attribute = SLUG_PARAMETERS.get(name, "id")
        value = await self._first_value(parent, attribute)
        if value is not None:
            return value
        # /api/v1/files/{id} has no list at its parent, but file_id does elsewhere
        if name == "id":
            inferred = f"{parent.rsplit('/', 1)[-1].removesuffix('s')}_id"
            if inferred == "course_id":
                return self._course_id
            if inferred in SELF_PARAMETERS:
                return SELF_PARAMETERS[inferred]
            name = inferred
        fallback = PARAMETER_LISTS.get(name)
        if fallback and self._course_id:
            return await self._first_value(fallback.replace("{course_id}", self._course_id))
        return None

    def _api(self, operation, client):
        if operation.api_class not in self._apis:
            module = importlib.import_module(operation.module)
            self._apis[operation.api_class] = getattr(module, operation.api_class)(client)
        return self._apis[operation.api_class]

    async def _call(self, operation, client):
        async with self._semaphore:
            try:
                self.result.outcomes[operation.name] = await self._call_operation(operation, client)
            except (aiohttp.ClientError, asyncio.TimeoutError, OSError) as error:
                self.result.outcomes[operation.name] = f"error:{type(error).__name__}"

    async def _call_operation(self, operation, client):
        reason = skip_reason(operation.route)
        if reason:
            return f"skipped:{reason}"

        values, missing = await self._resolve_path_values(operation.route)
        if values is None:
            return f"skipped:no_data:{missing}"

        api = self._api(operation, client)
        method = getattr(api, f"{operation.name}_with_http_info")
        raw_method = getattr(api, f"{operation.name}_without_preload_content")
        arguments, missing = self._arguments(method, values)
        if arguments is None:
            return f"skipped:required:{missing}"

        response = await raw_method(**arguments, _request_timeout=REQUEST_TIMEOUT)
        data = await response.read()
        status = response.status
        if not 200 <= status < 300:
            self.result.records.append(build_record(operation.route, status, self.role, None))
            return f"http_{status}"

        body = self._decode(data)
        self.result.records.append(build_record(operation.route, status, self.role, body))
        return await self._parse(operation, method, arguments)

    @staticmethod
    def _decode(data):
        try:
            return json.loads(data.decode().removeprefix("while(1);"))
        except (ValueError, UnicodeDecodeError):
            return None

    def _arguments(self, method, values):
        """Keyword arguments for an operation, or None and the name it can't fill."""
        arguments = {}
        for name, parameter in inspect.signature(method).parameters.items():
            if name.startswith("_") or name == "self":
                continue
            if name in values:
                arguments[name] = self._coerce(values[name], parameter)
            elif name == "per_page":
                arguments[name] = PER_PAGE
            elif name == "auto_mark_as_read":
                arguments[name] = False
            elif name == "context_codes" and self._course_id:
                arguments[name] = [f"course_{self._course_id}"]
            elif name in QUERY_VALUES:
                arguments[name] = QUERY_VALUES[name]
            elif parameter.default is inspect.Parameter.empty:
                return None, name
        return arguments, None

    @staticmethod
    def _coerce(value, parameter):
        return int(value) if "StrictInt" in str(parameter.annotation) and value.isdigit() else value

    async def _parse(self, operation, method, arguments):
        try:
            await method(**arguments, _request_timeout=REQUEST_TIMEOUT)
        except ValidationError as error:
            self.result.failures[operation.name] = parse_error_kinds(error)
            return "parse_failure"
        except (ValueError, TypeError, AttributeError, KeyError) as error:
            self.result.failures[operation.name] = [type(error).__name__]
            return "parse_failure"
        return "parsed"


def write_result(result, directory):
    """Write the role's report, and its evidence for the audit."""
    directory = pathlib.Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    report = {"role": result.role, "counts": result.counts(), "outcomes": result.outcomes, "failures": result.failures}
    (directory / f"contract-{result.role}.json").write_text(json.dumps(report, indent=2, sort_keys=True))
    with (directory / f"probes-{result.role}.jsonl").open("w") as probes:
        for record in result.records:
            probes.write(json.dumps(record) + "\n")
