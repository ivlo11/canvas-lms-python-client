# Proposal

## Why

Nine paginated operations, and six related media operations, return untyped `object` or `List[object]`. Their `@returns` tags name a model the generator never collects, so it falls back silently with no warning. There are three causes:

| Operations | `@returns` | Why it doesn't resolve |
|---|---|---|
| `media_objects_index` and its 5 context variants (paginated) | `[MediaObject]` | `MediaObject` is an `@object` example block, not a `@model` schema. The adapter collects only `@model`. |
| `media_tracks_index`, `media_tracks_update` (each with `_for_other`) | `[MediaTrack]` | Same: `MediaTrack` is an `@object` example. |
| `media_objects_update_media_object` (and `_for_other`) | none | No `@returns`, though it renders a media object. |
| `registrations_history` (paginated) | `[Lti::RegistrationHistoryEntry]` | No model by that name is documented. |
| `rubrics_api_used_locations` (and `_for_accounts`, paginated) | `UsedLocations` | No model by that name. The action also returns a list of courses, not one object, so no `_all` iterator is generated. |

Canvas's HTML docs treat `@object` and `@model` alike, which is why the gap goes unnoticed. The `MediaObject` example is also inaccurate: it shows `user_entered_title`, which the serializer never sends, and leaves out `created_at`, `embedded_iframe_url`, `auto_caption_status` and `viewer_restrictions`.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `media_objects_controller.rb`: replace `@object MediaObject` with a `@model MediaObject` schema matching `media_object_api_json`. Add `@returns MediaObject` to Update Media Object.
  - `media_tracks_controller.rb`: replace `@object MediaTrack` with a `@model MediaTrack` schema matching `media_track_api_json`.
  - `lti/registrations_controller.rb`: add `@model Lti::RegistrationHistoryEntry`, matching `lti_registration_history_entry_json`.
  - `rubrics_api_controller.rb`: add `@model RubricUsedLocation` (a course with its `assignments`) and change `@returns UsedLocations` to `@returns [RubricUsedLocation]`.
- **Generator (canvas-lms fork, fork-only commit):** when an `@returns` names a model that resolves to no collected schema, the adapter prints a warning naming the operation and the model. Generation still succeeds and the response stays untyped. The regenerated output lists the remaining unresolved names, which are left as a follow-up.
- **Seed script (fork, never committed):** new `--media-objects` and `--rubric-locations` options create a course media object with a caption track, and a rubric associated with an assignment, so both shapes can be checked against a live response.
- **Client:** regenerate.
  - The six media list operations yield `MediaObject`.
  - The media track operations return `List[MediaTrack]`.
  - Update Media Object returns `MediaObject`.
  - `registrations_history` yields `LtiRegistrationHistoryEntry`.
  - `rubrics_api_used_locations` pages are `List[RubricUsedLocation]` and gain `_all` iterators.
  - Offline tests use captured payloads, and integration tests cover history, used locations and media objects.
- **BREAKING (client):**
  - These operations change from `object`/`List[object]`/`None` to models.
  - `rubrics_api_used_locations` changes from one object per page to a list.
  - The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`:
  - media object, LTI registration history and rubric used-location lists yield typed items
  - the "undefined model yields raw items" requirement loses its only member (registration history) and is removed. The general fallback stays in `typed-operation-responses`.
- `typed-operation-responses`:
  - media object and media track operations return typed models
  - generation warns about `@returns` models that don't resolve

## Impact

- **canvas-lms (fork):**
  - Docs: `app/controllers/media_objects_controller.rb`, `media_tracks_controller.rb`, `lti/registrations_controller.rb`, `rubrics_api_controller.rb`.
  - Generator: `lib/swagger_yard/canvas_adapter.rb` and `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb` and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `api/media_objects_api.py`, `media_tracks_api.py`, `registrations_api.py` and `rubrics_api_api.py`. New models `MediaObject`, `MediaTrack`, `LtiRegistrationHistoryEntry` and `RubricUsedLocation`, plus inline item models, docs and test stubs.
  - `test/custom/unit/test_paginated_response_types.py`, a new unit test with fixtures, and `test/custom/integration/test_paginated_models.py`.
- **Dependencies:** none.
  - `type-nested-object-properties` (archived) touches nested object properties. This change uses only array items with `properties`, which already become models, and leaves `viewer_restrictions` as a plain mapping.
