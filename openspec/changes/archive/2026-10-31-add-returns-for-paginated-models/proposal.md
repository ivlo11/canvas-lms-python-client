# Proposal

## Why

An audit of the 196 `x-paginated` operations found 39 whose spec operation has no response schema. For those, the generated client builds an empty `_response_types_map`, so `response_deserialize` always returns `.data = None`, and the `_paginated` / `_all` generators return on the first page without yielding anything or raising an error. Callers see an empty result for endpoints that actually return data. For 5 of the underlying controller actions (7 client operations), canvas-lms already defines a `@model` that matches what the action renders. Only the `@returns` annotation is missing, so these are the cheapest and safest to fix first. This repeats the pattern already applied to `assignments_api_user_index`.

## What Changes

- **Cross-repo fix (canvas-lms fork):** add a `# @returns [Model]` line to five controller doc blocks:

  | Controller action | Annotation | Client operations fixed |
  |---|---|---|
  | `AppointmentGroupsController#index` | `@returns [AppointmentGroup]` | `appointment_groups_index` |
  | `AppointmentGroupsController#users` | `@returns [User]` | `appointment_groups_users` |
  | `AppointmentGroupsController#groups` | `@returns [Group]` | `appointment_groups_groups` |
  | `RubricsApiController#index` | `@returns [Rubric]` | `rubrics_api_index`, `rubrics_api_index_for_courses` |
  | `Lti::LtiAppsController#launch_definitions` | `@returns [Lti::LaunchDefinition]` | `lti_apps_launch_definitions`, `lti_apps_launch_definitions_for_accounts` |

- Regenerate `public/doc/openapi/canvas.openapi.yaml`, then regenerate this client.
- For the four non-LTI rows, the base method's return type changes from `None` to `List[Model]`, `_paginated` changes from `AsyncIterator[Any]` to `AsyncIterator[List[Model]]`, and `_all` changes from `AsyncIterator[Any]` to `AsyncIterator[Model]`.
- For the LTI row, the operations change from `None` / `AsyncIterator[Any]` to `List[object]` / `AsyncIterator[List[object]]` / `AsyncIterator[object]`. They yield raw dicts instead of nothing. Typing them as `LtiLaunchDefinition` is blocked by a generator bug in resolving namespaced models (see Impact).
- Add an offline regression test that fails when any `x-paginated` operation in the generated client has an empty response types map, with an explicit allowlist for the 32 operations this change leaves untyped. The allowlist should shrink over time.

## Capabilities

### New Capabilities
- `paginated-list-responses`: the client's contract that paginated operations deserialize each page into the documented response type and yield it, rather than ending silently with no items.

### Modified Capabilities
- `integration-testing`: adds requirements (existing ones unchanged) for an optional `CANVAS_ADMIN_API_TOKEN` used by admin-scoped tests (account rubrics, account LTI launch definitions, appointment groups), which the existing observer token cannot read. Also requires tests to skip, not fail, when seeded data is absent.

## Impact

- **canvas-lms (fork):** five comment-only lines in `app/controllers/appointment_groups_controller.rb`, `app/controllers/rubrics_api_controller.rb`, and `app/controllers/lti/lti_apps_controller.rb`, plus the regenerated OpenAPI spec. Canvas runtime behavior does not change.
- **canvas-lms-python-client:**
  - Regenerated `api/appointment_groups_api.py`, `api/rubrics_api_api.py`, `api/lti_apps_api.py` and their docs. Callers that iterated these operations and got nothing will now receive items. Callers that relied on a `None` return will now get a list, which is a behavior change but not a meaningful break, since these endpoints never returned useful data before.
  - New custom test modules `src/canvas_lms_python_client/test/test_paginated_response_types.py` (offline) and `test/test_integration_paginated_models.py` (integration). Both must be added to `src/.openapi-generator-ignore` and to the README's "Custom, never overwritten" list.
  - `test/conftest.py`: new `canvas_admin_api_client` fixture. README "Integration Tests": document `CANVAS_ADMIN_API_TOKEN`.
- **Strict models:** `User`, `Group`, `AppointmentGroup`, and `Rubric` use strict pydantic types. A mismatch between a `@model` and the live JSON will now raise during deserialization instead of being hidden by `None`. Integration verification against the seeded Canvas covers this.
- **Out of scope (follow-ups):**
  - *Namespaced model refs:* `model_schema_exists?` in `lib/swagger_yard/canvas_adapter.rb` looks up `Lti::X`, but schemas are registered as `Lti_X`. As a result every `@returns [Lti::…]` currently emits `type: object`. This also affects `deployments_list`, `context_controls_index`, `resource_links_index`, and others.
  - *Wrapped responses* (`{"polls": [...]}`, JSON-API `serialize_jsonapi`, `{events, linked}`): 10 polling/quiz/outcome/grading-period/pace/audit actions. A bare `@returns [Model]` would make deserialization fail, so they need a wrapper model and a way for `_all` to unwrap it.
  - *No matching model:* discussion entries, planner items, TODO items, logins, conversation batches, recipients, bulk user progress, `search#all_courses`, and `multiple_gradeable_students`. The last one has `UserDisplay`, but `UserDisplay` would drop the endpoint's `assignment_ids` field.
  - *Generator mis-attribution:* `/api/v1/users/self/todo` is emitted as `ServiceCredentials-todo_items` with `x-controller: user_observees` / `x-action: show_observer`, but the route is `users#todo_items`.
