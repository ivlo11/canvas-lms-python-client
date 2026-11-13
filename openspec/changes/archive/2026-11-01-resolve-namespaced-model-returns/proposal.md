# Proposal

## Why

Canvas documents LTI responses with namespaced model names, for example `@returns [Lti::Deployment]`. The spec generator registers those models as component schemas under sanitized names (`Lti_Deployment`). When it resolves `@returns`, though, it looks up the raw name (`Lti::Deployment`), never finds it, and falls back to `type: object`. As a result, 32 operations whose Canvas docs name an existing model are untyped in the client and return raw dicts. Six of them are paginated list endpoints. The fix is one name normalization in the generator. It also exposes Canvas doc errors that are hidden today: two endpoints documented as returning a single object actually return arrays, and at least one LTI model field has the wrong type (`Lti::LaunchDefinition.definition_id` is documented as a string, but Canvas sends an integer). Typing these responses without correcting those errors would turn working calls into `ValidationError`s.

## What Changes

- **canvas-lms generator (fork):** `@returns` model resolution in `lib/swagger_yard/canvas_adapter.rb` uses the same name sanitization as schema registration (`::` → `_`). It does so for both the existence check and the model name recorded for the `$ref`. Non-namespaced names behave exactly as before.
- **canvas-lms generator (fork), `string|Model` properties:** a property documented as `"type": "string|Model"` with a `$ref` becomes `oneOf: [string, $ref Model]` instead of a bare `$ref`. LTI `created_by` / `updated_by` are a `User` or the string `"Instructure"` (design D5).
- **canvas-lms docs (fork), `@returns` corrections:**
  - `Lti::ContextControlsController#create_many`: `Lti::ContextControl` → `[Lti::ContextControl]`
  - `Lti::ResourceLinksController#bulk_create`: `Lti::ResourceLink` → `[Lti::ResourceLink]`

  Both render arrays (`controls.map`, `links.map`).
- **canvas-lms docs (fork), `@model` type corrections:** change field types in the 7 resolving LTI models (`Lti::Deployment`, `Lti::ContextControl`, `Lti::LaunchDefinition`, `Lti::Registration`, `Lti::RegistrationAccountBinding`, `Lti::OverlayVersion`, `Lti::ResourceLink`) wherever they differ from what Canvas sends. Live, seeded responses are the evidence, as in `fix-polling-and-quiz-model-types`. Found by the captures: `Lti::LaunchDefinition.definition_id` is always an integer (`Lti::AppLaunchCollator` sends `tool.id` or `message_handler.id`); `Lti::OverlayVersion.diff` holds tuples of mixed values; and `Lti::RegistrationAccountBinding.created_by` / `updated_by` can be the string `"Instructure"`. No Ruby code changes.
- Regenerate the spec and the client. The 32 operations become typed:

  | Group | Operations | New client type |
  |---|---|---|
  | Paginated lists (6) | `deployments_list`, `deployments_list_controls`, `context_controls_index`, `lti_apps_launch_definitions` (+ `_for_accounts`), `resource_links_index` | `List[LtiDeployment]` (`deployments_list`, and `context_controls_index`, which groups controls by deployment) / `List[LtiContextControl]` / `List[LtiLaunchDefinition]` / `List[LtiResourceLink]` |
  | Context controls (5) | `create`, `show`, `update`, `delete`, `create_many` | `LtiContextControl` (`create_many`: `List[LtiContextControl]`) |
  | Deployments (3) | `create`, `show`, `destroy` | `LtiDeployment` |
  | Registrations (13) | `create`, `show`, `update`, `destroy`, `show_by_client_id`, `show_by_utid`, `install_status`, `reset`, `install_from_template`, `apply_registration_update_request`, `bind`, `unbind`, `overlay_history` | `LtiRegistration`, `LtiRegistrationAccountBinding`, `List[LtiOverlayVersion]` |
  | Resource links (5) | `create`, `show`, `update`, `destroy`, `bulk_create` | `LtiResourceLink` (`bulk_create`: `List[LtiResourceLink]`) |

- **BREAKING (client types):** these operations' return types change from `object` / `List[object]` to models, so callers that indexed into dicts must use attributes instead. The client has not been published, so `packageVersion` is not bumped (same as `fix-polling-and-quiz-model-types`).
- Not typed, and unchanged: `registrations_history` (`Lti::RegistrationHistoryEntry` has no `@model`), and `registrations_show_registration_update_request` / `_latest_registration_update_request` (`Lti::RegistrationUpdateRequest` has no `@model`).

## Capabilities

### New Capabilities
- `typed-operation-responses`: operations whose Canvas docs name an existing model return that model, whether the name is namespaced or not, and whether the response is a single object or a list. Operations whose named model does not exist remain untyped rather than failing.

### Modified Capabilities
- `paginated-list-responses`: LTI launch definitions and the other LTI list endpoints join the typed-items requirement. The "documented but unresolved model yield raw items" requirement is replaced by "documented model is undefined yield raw items", whose scenario uses LTI registration history, because "unresolved" was really a generator bug.

## Impact

- **canvas-lms (fork):**
  - `lib/swagger_yard/canvas_adapter.rb` (resolution and `string|Model` oneOf), plus specs in `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
  - Doc-comment edits in `app/controllers/lti/context_controls_controller.rb`, `resource_links_controller.rb`, `lti_apps_controller.rb`, and the controllers that declare the other LTI `@model`s, where corrections are needed.
  - Regenerated `public/doc/openapi/canvas.openapi.yaml`.
  - A seed helper for LTI data in `spec/manual_seeding/large_gradebook_seeds.rb`, used for live verification. It is left uncommitted, following the previous change's precedent.
- **canvas-lms-python-client:**
  - Regenerated `api/context_controls_api.py`, `deployments_api.py`, `lti_apps_api.py`, `registrations_api.py`, `resource_links_api.py`, and affected `models/lti_*.py` and docs. One new oneOf wrapper model, `LtiRegistrationCreatedBy`, shared by the 5 `created_by` / `updated_by` properties.
  - `test/test_integration_paginated_models.py`: the LTI launch-definition tests assert `LtiLaunchDefinition` models instead of dicts.
  - New offline payload tests and new integration tests for the LTI list endpoints.
- Non-LTI operations: no change is expected. Verify that the spec diff contains only LTI operations and the corrected models.
