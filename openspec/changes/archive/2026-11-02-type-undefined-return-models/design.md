# Design

## Context

- Motivation and the list of operations: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md` and `specs/typed-operation-responses/spec.md`.
- **How models are collected.** `CanvasAdapter.collect_model_schemas!` reads only `@model` tags (`canvas_adapter.rb:212`). `doc/api/documentation_helpers.rb:60` indexes `@object` and `@model` together for the HTML docs. `@object` appears exactly twice in the codebase: `MediaObject` and `MediaTrack`.
- **How an unknown `@returns` model degrades.** `handle_array_response` and `handle_primitive_or_model_response` emit `array<object>` / `object` when `model_schema_exists?` is false, and nothing is printed. The only existing warning convention is `puts "[warn]: ..."` (`canvas_adapter.rb:820`).
- **What Canvas sends**, read from the serializers:
  - **`MediaObject`** (`media_object_api_json`):
    - always: `media_id`, `created_at`, `media_type`, `title`, `can_add_captions`, `embedded_iframe_url`, `auto_caption_status`, `viewer_restrictions` (object)
    - only when the media object has a status: `status`
    - unless excluded: `media_sources[]` (Kaltura flavors plus `src` and `label`) and `media_tracks[]` (`kind`, `created_at`, `updated_at`, `id`, `locale`, `workflow_state`, `asr`, `url`, plus `inherited` on attachment routes)

    It never sends `user_entered_title`, although the `@object` example shows it.
  - **`MediaTrack`** (`media_track_api_json`): `id`, `locale`, `kind`, `workflow_state`, `asr`, `media_object_id`, `user_id`. With `include[]`, also `content`, `webvtt_content`, `created_at`, `updated_at`. This is a different shape from the track items nested in `MediaObject`.
  - **`Lti::RegistrationHistoryEntry`** (`lti_registration_history_entry_json`): `id`, `root_account_id`, `lti_registration_id`, `created_at`, `updated_at`, `diff`, `update_type`, `comment`, `old_configuration`, `new_configuration`, `created_by`, `old_controls_by_deployment`, `new_controls_by_deployment`. Captured live from registration 1:
    - `created_by` is the string `"Instructure"`; for non-site-admin editors it's a user JSON object
    - `*_controls_by_deployment` items are `Lti::Deployment`-shaped, with `context_name`, `workflow_state` and `context_controls`
    - `update_type` is one of `manual_edit`, `registration_update`, `bulk_control_create`, `control_edit`
  - **Used locations** (`used_locations_to_json`): a paginated array of `course.as_json(only: [:id, :name], methods: [:concluded?])` plus `assignments: [{id, title}]`. The concluded key is literally `concluded?`.
- **Live data:** before this change the seeded instance had LTI history entries, but no media objects (course 5) and no rubrics in courses 2 and 5. Task 1.1 seeds both; course media listing returns 500 in dev (no Kaltura) unless `exclude[]=sources` is passed.

## Goals / Non-Goals

**Goals:**
- The 9 paginated operations and the 6 media operations return models that match what Canvas sends.
- Unknown `@returns` model names are visible in generator output, so the rest can be fixed later.

**Non-Goals:**
- The ~13 other unresolved names the warning will list (`AiConversation`, `RubricImport`, `Lti::RegistrationUpdateRequest`, …): follow-up.
- Media track create, create-ASR and destroy (`@returns MediaObject | MediaTrack`), which have no `@API` tag and aren't in the client.
- Inferring schemas from `@object` examples (option B in the explore).
- Making generation fail on unresolved models.

## Decisions

### D1: `@object` → `@model` for `MediaObject` and `MediaTrack`
Replace each `@object` example block with a `@model` JSON schema in the same controller, keeping the model name and the description text as `description`s:
- **`MediaObject`:**
  - properties as listed in Context; all optional, because `exclude[]` and `status` make fields conditional
  - `media_sources` and `media_tracks` are arrays of inline objects with `properties`, so they become inline item models without depending on `type-nested-object-properties`
  - `viewer_restrictions` is an `object` without `properties`, so it stays a mapping
  - nested `media_tracks` item dates are `"type": "string", "format": "date-time"`, because array items with `properties` pass through unconverted, so `datetime` would be an invalid OpenAPI type there
  - `media_sources` flavor fields (`height`, `width`, `bitrate`, `size`, `isOriginal`) are typed `string`, as Kaltura sends them and as the existing example shows; dev has no Kaltura, so D6 can't confirm this
- **`MediaTrack`:** properties as listed in Context, all optional except `id`, `locale` and `kind`.
- Add `@returns MediaObject` to Update Media Object.
- Seeded media is owned by Seeded Admin 2 (user 392), so fixtures carry no real user data.
- *Alternative: adapter infers schemas from `@object` examples.* Rejected: it covers only two blocks, example values are a weak type source, and the `MediaObject` example is wrong (`user_entered_title`).
- *Alternative: reference `MediaTrack` from `MediaObject.media_tracks`.* Rejected: the nested items carry `url`/`asr`/`inherited` and lack `media_object_id`/`user_id`.

HTML docs change from an example block to a fields table, as for every other `@model`.

### D2: `@model Lti::RegistrationHistoryEntry`
Add it next to the other `Lti::` models in `lti/registrations_controller.rb`, keeping `@returns [Lti::RegistrationHistoryEntry]`:
- integer ids
- `created_at`/`updated_at` as `datetime`
- `update_type`, `comment` as `string`; the four valid values go in the description, not an `enum`, so a new Canvas value doesn't break deserialization
- `diff`, `old_configuration` and `new_configuration` as `object` without `properties`, because they're free-form
- `created_by` is `"type": "string|User"` with `"$ref": "User"`, because it's a user object or the string `"Instructure"`. The adapter already turns that into a `oneOf` (the `Lti::OverlayVersion.created_by` precedent), so the client keeps both forms. *Amended during apply:* the first draft left it untyped (`Any`) on the assumption that `oneOf` needed adapter support.
- `old_controls_by_deployment`/`new_controls_by_deployment` as arrays of `"$ref": "Lti::Deployment"`; the live payload matches that model's documented fields

### D3: `@model RubricUsedLocation` and a list return
In `rubrics_api_controller.rb`:
- add `@model RubricUsedLocation` with `id` (integer), `name` (string), `concluded?` (boolean) and `assignments`, an array of inline `{id: integer, title: string}`
- change `@returns UsedLocations` to `@returns [RubricUsedLocation]`
- *Amended during apply:* `Rubric.points_possible` changes from `integer` to `number`. The seeded rubric showed Canvas sends `10.0`, which failed `test_course_rubrics_typed` and the used-locations flow.

The property name is `concluded?`, because that is the key Canvas sends. openapi-generator turns it into a valid Python name with the JSON alias `concluded?`. Task 3.1 records the generated attribute name.
- *Alternative: name it `UsedLocations` and keep it singular.* Rejected: the response is an array of courses, and a singular name reads like the whole response.

### D4: Unresolved-model warning
In `process_returns_tags`, after the model name is extracted for a non-inline `@returns`:
- warn when the type text looks like a model reference and `resolve_schema_name` doesn't find it
- a model reference is an identifier with optional `::` segments, optionally in `[]` or `Array<>`, after unions are split on `|`, and not a primitive name
- the message is `[warn]: unresolved @returns model <name> for <operation_id>`
- generation also prints a final count

Prose returns (`the input arguments …`, `204 No Content`), primitives, and inline objects are skipped. The adapter spec covers:
- an undefined list model warns
- a defined, namespaced or `Schemas::Docs::` model doesn't warn
- prose and primitives don't warn

The adapter change is a fork-only commit, separate from the docs. It also touches `open_api_generator.rb` for the summary count, so the commit has three files.
- *Alternative: fail generation.* Rejected: about 13 names are still unresolved, and generation has to keep working while they're fixed.

### D5: Seed options
`--media-objects` (standalone, idempotent):
- for the seeded admin and course 5, find or create a `MediaObject` (`media_id: "m-seeded-media-1"`, `media_type: "video"`, `title`, `user`, `context: course`)
- link it with a media `Attachment` in the course (`media_entry_id` = the media id), because course listing goes through attachments
- give it a `subtitles` track (`locale: "es"`, small WebVTT `content`)
- print the ids

`--rubric-locations` (standalone, idempotent):
- find or create a rubric in course 5
- associate it with one of the course's assignments (`RubricAssociation`, purpose `grading`)
- print the rubric id

Neither is committed.

### D6: Verification against live payloads
After seeding, capture these with the admin token:
- the course media objects list
- the media tracks list (with `include[]=content`)
- the registration history
- the rubric used locations

Before writing the docs, record each field's JSON type next to the planned schema type. Save the payloads as fixtures under `test/custom/unit/fixtures/return_models/` for `test/custom/unit/test_return_models.py`, which checks that:
- each payload deserializes into its model with values equal to the JSON
- `created_by` keeps both the string and the object form; a synthetic object-form entry is added because live data only has the string
- the used-locations items keep `concluded?` and their assignments

Integration tests in `test/custom/integration/test_paginated_models.py` cover the three paginated scenarios. Each skips with a seed hint when the seeded data is missing.

### D7: Client test updates
- `LTI_LIST_ITEM_TYPES["registrations_history"]` becomes `"LtiRegistrationHistoryEntry"`, and its comment is removed.
- A parallel mapping asserts the page item types of the six media list operations (`MediaObject`) and `rubrics_api_used_locations` (`RubricUsedLocation`).
- `test_all_iterator_only_for_list_responses` already checks that `rubrics_api_used_locations_all` now exists.
- `UNDOCUMENTED_PAGINATED_OPERATIONS` is unchanged: these operations had response types (`object`), they just weren't models.

## Risks / Trade-offs

- [Kaltura flavor fields are untestable in dev] → They're typed `string`, per the existing example and Kaltura's API. All are optional, and a mismatch would show up as a `ValidationError` against a real instance (follow-up if it happens).
- [`created_by` as a `oneOf`] → Callers check `created_by.actual_instance` for `str` or `User`. Live data only has the string, so a synthetic user entry covers the object form.
- [The `concluded?` property name generates an awkward attribute] → The alias keeps the wire name. The generated name is recorded, and a doc rename isn't possible because Canvas sends that key.
- [Warning noise from prose `@returns`] → Only model-like references are matched, and the adapter spec pins the prose cases.

## Migration Plan

1. Fork:
   1. seed (uncommitted) and capture the payloads
   2. edit the docs, regenerate (uncommitted), diff, commit the docs in upstream format
   3. add the warning with adapter specs, regenerate, record the warnings, commit (fork format)
2. Client: regenerate, update the tests and fixtures, run the offline and integration suites, commit.

Rollback: revert the commits. The seed data is dummy data.
