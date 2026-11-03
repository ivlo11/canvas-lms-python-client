# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Re-read `spec/manual_seeding/large_gradebook_seeds.rb`. Add the standalone `--media-objects` and `--rubric-locations` options (D5) as additive edits. Run each twice in the web container with `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --media-objects` (then `--rubric-locations`). Verify that the first run prints the media object, track and rubric ids, and the second run creates nothing new. Do not commit the script.
  - Done. Media object 1 (`m-seeded-media-1`, owned by Seeded Admin 2, user 392), attachment 1 and `es` track 1 in course 5; rubric 1 in course 5 associated with assignment 52. Second runs create nothing new.
- [x] 1.2 Capture these payloads (D6) with the admin token:
  - `GET /courses/5/media_objects`
  - `GET /media_objects/:media_id/media_tracks?include[]=content&include[]=created_at`
  - `GET /accounts/1/lti_registrations/1/history`
  - `GET /courses/5/rubrics/:id/used_locations`

  In these notes, record each field's JSON type next to the planned schema type from D1–D3, and note any field the serializer reading missed. If a shape differs from the design, update D1–D3 before task 2.1.
  - Done. Course media listing returns 500 in dev (no Kaltura), so it was captured with `exclude[]=sources`; `media_sources` is checked with a synthetic item from the docs example.
  - MediaObject: `media_id`, `created_at`, `media_type`, `title`, `embedded_iframe_url` str; `can_add_captions` bool; `auto_caption_status` null; `viewer_restrictions` `{}`; track items int `id`, str `kind`/`locale`/`workflow_state`/`url`/dates, bool `asr`.
  - MediaTrack: int `id`/`media_object_id`/`user_id`; str `locale`/`kind`/`workflow_state`/`content`/dates; bool `asr`; `webvtt_content` null.
  - History: int ids; dict `diff`; `update_type` `control_edit`; `comment` and configurations null; `created_by` `"Instructure"`; `*_controls_by_deployment` `Lti::Deployment`-shaped.
  - Used locations: `{id: int, name: str, "concluded?": bool, assignments: [{id: int, title: str}]}`.
  - Shapes match D1–D3. Found during 4.3: `Rubric.points_possible` is a float (`10.0`), fixed in 2.1 (D3 amended).

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1 to `media_objects_controller.rb` and `media_tracks_controller.rb`, D2 to `lti/registrations_controller.rb`, and D3 to `rubrics_api_controller.rb`. Verify:
  - `git diff` shows comment lines only
  - `grep -rnE "^\s*#\s*@object " app/controllers` has no hits
  - each new model's JSON parses (extract the block and run it through `JSON.parse` in the web container)
  - Done. Comment-only diff, no `@object` left, all four blocks parse. Also `Rubric.points_possible` → `number`, and `created_by` as `string|User` (D2 amended).
- [x] 2.2 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and diff it with the previous spec. Verify:
  - schemas `MediaObject`, `MediaTrack`, `Lti_RegistrationHistoryEntry` and `RubricUsedLocation` exist
  - the six media list operations, the two media track operations (and their `_for_other` routes), Update Media Object, registration history and used locations reference them, with arrays where D1–D3 say so
  - no other operation's response changed
  - Done. Added `Lti_RegistrationHistoryEntry`, `MediaObject`, `MediaTrack`, `RubricUsedLocation`; `Rubric` changed only `points_possible`; 15 operations changed, `paths` otherwise equal; no invalid types.
- [x] 2.3 Commit only the four controller files in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only those files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.
  - Done: `5f27c956e58 fix(canvas-lms): document media, history and rubric models` (four controllers).

## 3. Unresolved-model warning (canvas-lms fork)

- [x] 3.1 Implement D4 in `lib/swagger_yard/canvas_adapter.rb`, with examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`:
  - an undefined list model warns
  - an undefined single model warns
  - defined, namespaced and `Schemas::Docs::` models don't warn
  - prose, primitive and inline-object `@returns` don't warn

  Run the adapter spec in the web container and verify that it passes.
  - Done. `rspec spec/lib/swagger_yard`: 173 examples, 0 failures. No new rubocop offenses.
- [x] 3.2 Regenerate and verify:
  - the output lists unresolved-model warnings and a count
  - none names an operation fixed in group 2
  - the spec file is byte-identical to the 2.2 output (the warning changes nothing else)

  Record the warned model names in these notes for the follow-up.
  - Done. 18 warnings, spec byte-identical, none from group 2. Names: `AccessibilityResourceScan`, `AiConversation`, `ApiRegistration`, `AssistResponse`, `JSON`, `LmgbUserDetails`, `Lti::RegistrationUpdateRequest`, `MasteryDistributionResponse`, `QueryResultsResponse`, `RollupJob`, `RubricImport`.
- [x] 3.3 Commit the adapter and spec in the fork's format (lines under 60 characters, the why, a test plan). Verify that `git log -1 --stat` lists only those two files.
  - Done: `ea3470ec099 feat(swagger_yard): warn about unresolved @returns`. Three files: the adapter, its spec, and `open_api_generator.rb` for the summary count (D4 amended).

## 4. Client (canvas-lms-python-client)

- [x] 4.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `media_objects_index_all` yields `MediaObject`
  - `media_tracks_index` returns `List[MediaTrack]`
  - `media_objects_update_media_object` returns `MediaObject`
  - `registrations_history_all` yields `LtiRegistrationHistoryEntry`
  - `rubrics_api_used_locations_all` exists and yields `RubricUsedLocation`

  Record the generated attribute name for `concluded?` in these notes.
  - Done. All five checks hold. `concluded?` generates attribute `concluded` with `alias="concluded?"`.
- [x] 4.2 Add the 1.2 fixtures under `test/custom/unit/fixtures/return_models/` and `test/custom/unit/test_return_models.py` (D6), and update `test_paginated_response_types.py` (D7). Verify that the new tests pass, and that they fail against the pre-change generated `api/` and `models/` files: check out the old files, confirm the failure, then restore them.
  - Done. New tests pass; against the pre-change `api/`/`models/`, `test_return_models.py` fails to import and two paginated-type tests fail. Fixtures hold no real user data (the synthetic `created_by` user is Seeded Admin 2).
- [x] 4.3 Add integration tests to `test/custom/integration/test_paginated_models.py` for course media objects, registration history and rubric used locations (D6). Run `pdm run pytest --integration -v -k "media or history or used_locations"` with the admin token and verify they pass. Verify that, without the seed data, they skip with a hint naming the seed option.
  - Done. Three tests added with a `require_seeded` skip hint naming the seed option; they pass with the admin token.
- [x] 4.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run (all three tokens set) shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.
  - Done. Offline: 3756 passed, 168 skipped. Integration: 27 passed, 5 skipped (`test_course_rubrics_typed` now passes). ruff clean. Commit `65a6e35 fix(canvas_lms_python_client): type media, history and rubric location models`. Regenerating from the main checkout's spec leaves only the usual `FILES` test-entry drop (discarded).

## 5. Final checks

- [x] 5.1 Run `openspec validate type-undefined-return-models --strict` and verify that it passes.
  - Done. `openspec validate type-undefined-return-models --strict` passes.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit onto instructure/canvas-lms `master` after signing the CLA. The task 3.3 commit stays in the fork.
- Fix the remaining unresolved `@returns` names the warning lists in task 3.2.
- Archive with `/opsx:archive` after review.
