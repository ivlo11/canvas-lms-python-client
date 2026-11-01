# Proposal

## Why

Canvas documents some responses inline as an object, for example `@returns { "account_calendars": [AccountCalendar], "total_results": "integer" }`. The spec generator reads every such `@returns { ... }` as a list of untyped objects. So the client deserializes the JSON object as a list and returns only its key names (`['account_calendars', 'total_results']`). The data is lost silently. That happens on 20 operations today, including the paginated `account_calendars_api_index`.

## What Changes

- **canvas-lms generator (fork), shape fix:** a `@returns` whose text starts with `{` always produces an object response, never a list. This alone stops the data loss on all 20 operations.
- **canvas-lms generator (fork), typed inline objects:** a new parser reads the raw `@returns { ... }` text. When every entry is `key: [Model]`, `key: Model`, `key: <primitive type>` or `key: <primitive literal>`, the operation returns a generated wrapper model with one optional property per key:
  - `[Model]` and `Model` must name an existing schema (namespaced names included).
  - The primitive types are `integer`, `string`, `boolean` and `number`. They may be quoted, and case doesn't matter (`String`).
  - A literal's type is inferred from its value: `true`/`false` → boolean, a quoted value → string, a whole number → integer.
  - Wrappers get no `required` keys (Canvas marks none) and no `additionalProperties`.
  - Anything else (`{Object}` with prose, unions, nested inline objects) stays a plain object.
  - This parser is separate from change 2's `@example_response` inference, which stays as it is.
- **Wrapper naming:** every generated wrapper, new ones and change 2's existing ones alike, is named `<Controller><Action>Response` after the Canvas controller and Rails action that return it (`AccountCalendarsApiIndexResponse`, `PollSessionsOpenedResponse`). Routes of the same action share one wrapper. Different actions get different wrappers, even when their shapes are identical. A name therefore never depends on what else the generator sees.
- **Typed by this change (10):**
  - `account_calendars_api_index` (paginated) and `visible_calendars_count`
  - `content_shares_unread_count`
  - `career_experience_enabled`, `switch_experience` and `switch_role`
  - `what_if_grades_api_update` and `reset_for_student_course`
  - `communication_channels_delete_push_token` (literal `true`)
  - `discovery_pages_api_token` (literal string)
- **Plain object, no longer a list (10):** the 8 AI conversation operations, `registrations_validate_lti_configuration` (a union) and `registrations_check_domain_duplicates` (a nested inline object).
- **BREAKING (client):**
  - Change 2's 14 wrapper models are replaced by one model per controller and action, for example `PollsResponse` → `PollsIndexResponse`, `PollsCreateResponse`, ….
  - The 20 operations above change their return type from `List[object]` to a model or a dict.
  - The client has never been released and has no consumers, so there is no version bump and no breaking-change documentation.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `typed-operation-responses`: adds requirements that an inline-object response is returned as an object, typed when its entries are typeable, and that wrapper models are named after their controller and action.
- `paginated-list-responses`: the wrapped-list requirement names each wrapper after its controller and action instead of sharing one wrapper across related operations, and adds the account calendars page, whose wrapper comes from an inline `@returns`.

## Impact

- **canvas-lms (fork):**
  - `lib/swagger_yard/canvas_adapter.rb`:
    - `process_returns_tags` handles the brace form from the raw docstring.
    - A new inline-object parser.
    - `register_wrapper_schema` takes the controller and action.
    - Change 2's `infer_wrapped_list_response` passes them.
  - New and updated examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
  - The regenerated `public/doc/openapi/canvas.openapi.yaml`.
  - No controller edits.
- **canvas-lms-python-client:**
  - Regenerated `models/`, `api/` and `docs/`. The 14 old wrapper modules are deleted as orphans. New wrapper modules are added.
  - `test/test_paginated_response_types.py`: wrapper names, `account_calendars_api_index` paginated typing.
  - `test/test_integration_paginated_models.py`: wrapper imports.
  - A new offline test for inline-object responses.
  - README "Wrapped List Responses": the example wrapper name.
- **Sequencing:** builds on `fix-nested-class-api-groups`, whose fork commit has landed (its client changes are still uncommitted in the working tree). It also regenerates the client alongside `generalize-union-property-types`.
