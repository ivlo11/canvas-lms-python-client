# Tasks

## 1. Inline-object @returns and wrapper naming (canvas-lms fork)

- [ ] 1.1 Before changing any code, confirm that `fix-nested-class-api-groups`'s client changes are committed (`git status` in the client shows none of its files), then capture the baseline. Using a throwaway script, write `operationId → response schema (JSON)` for every operation in `public/doc/openapi/canvas.openapi.yaml` to the scratchpad. Verify that it shows the 20 brace operations (design, Context) as `array` of `object`, and the 14 change 2 wrappers by their key names.
- [ ] 1.2 In `spec/lib/swagger_yard/canvas_adapter_spec.rb`, add `describe "inline object @returns"` with `YARD.parse_string` fixtures covering:
  - the D2 grammar: quoted and bare keys, `[Model]`, `Model`, a namespaced model, `"integer"`, `String`, `true`, `"eyJ..."` and `42`
  - each rejection: `{Object} prose`, a union with `|`, a nested object, `[String]`, an unknown model, `{A, B}`, and one bad entry among good ones
  - D3's plain-object outcome
  - D4 naming: two actions with the same shape, route aliases sharing, and the refuse-a-different-schema warning

  Update the existing `.register_wrapper_schema` and change 2 examples to the new names. Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that the new examples fail before 1.3.
- [ ] 1.3 Implement D1–D5 in `lib/swagger_yard/canvas_adapter.rb`:
  - raw-docstring brace detection in `process_returns_tags`
  - the inline-object parser
  - `register_wrapper_schema(name, properties, source)`
  - the resource + Rails-action name, used by both the new path and `infer_wrapped_list_response`

  Leave `WRAPPED_LIST_EXAMPLE` and change 2's trigger unchanged. Verify that `bin/rspec spec/lib/swagger_yard/` passes and that `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb` is clean.
- [ ] 1.4 Regenerate the spec in the web container (`bundle exec rake doc:openapi`) and run the D6 comparison against the 1.1 baseline. Verify:
  - These 10 operations have a wrapper `$ref`: `AccountCalendarsApi-index`, `-visible_calendars_count`, `ContentShares-unread_count`, `CareerExperience-enabled`, `-switch_experience`, `-switch_role`, `WhatIfGradesApi-update`, `-reset_for_student_course`, `CommunicationChannels-delete_push_token` and `DiscoveryPagesApi-token`. Their properties match the docs, `success` is boolean and `token` is string.
  - The 8 `AiConversations-*`, `Registrations-validate_lti_configuration` and `Registrations-check_domain_duplicates` are `type: object`.
  - Every change 2 operation references `<Resource><Action>Response` with properties identical to its old wrapper, and route aliases share one name.
  - No other operation's response changed, and no change 2 `<Key>Response` schema remains.

  Record the new wrapper count in these notes.
- [ ] 1.5 Commit in the fork following its commit guidelines: generator, its spec, and the regenerated YAML. Verify with `git log -1 --stat` that no controller files are included.

## 2. Regenerate the client and remove orphans (canvas-lms-python-client)

- [ ] 2.1 Copy `src/.openapi-generator/FILES` to the scratchpad, then regenerate the client (`openapi-generator-cli generate` with `openapi-generator-config.yaml`, `-t mustache-templates`, `-o src`). Verify that `models/account_calendars_api_index_response.py` and `models/polls_index_response.py` exist.
- [ ] 2.2 Delete the files listed in the old `FILES` but not the new one, skipping `src/.openapi-generator-ignore` paths (D7). Verify that `models/polls_response.py` and the other 13 old wrapper modules, their docs and their generated tests are gone, and that `git status` shows no custom file deleted.
- [ ] 2.3 Verify the generated signatures:
  - `account_calendars_api_index_paginated` is `AsyncIterator[AccountCalendarsApiIndexResponse]` and has no `_all`.
  - `content_shares_unread_count` returns `ContentSharesUnreadCountResponse`.
  - `ai_conversations_show` returns `object`, not `List[object]`.

## 3. Client tests and docs (canvas-lms-python-client)

- [ ] 3.1 Update `test/test_paginated_response_types.py`:
  - Key `WRAPPED_LIST_RESPONSES` by the new wrapper names, one entry per wrapper, and add `AccountCalendarsApiIndexResponse`.
  - Confirm that `account_calendars_api_index` is not on `UNDOCUMENTED_PAGINATED_OPERATIONS`.

  Verify that the module passes, including `test_all_iterator_only_for_list_responses`.
- [ ] 3.2 Add `test/test_inline_object_responses.py` (custom; add it to `src/.openapi-generator-ignore`). It checks offline:
  - The return annotation of each of the 20 operations.
  - Each typed wrapper deserializes its documented shape: the `account_calendars` list items are `AccountCalendar`, `total_results` is an int, `success` is a bool, and `token` is a str. An omitted key leaves its attribute `None`.
  - For each of the 10 plain-object operations, `ApiClient` deserializes `{"a": 1, "b": [2]}` to that same mapping.

  Verify that it passes, and that the plain-object case fails against the pre-change client: check out the old API module, confirm the failure, then restore it.
- [ ] 3.3 Update `test/test_integration_paginated_models.py` imports and assertions to the new wrapper names, and add `test_account_calendars_pages_typed` (admin client: each page is `AccountCalendarsApiIndexResponse` with `AccountCalendar` items and an int `total_results`). Verify with `pdm run pytest --integration -m integration -v` against the seeded instance. Record any strict-model `ValidationError` as a follow-up naming the model and field.
- [ ] 3.4 Update the README "Wrapped List Responses" example to the new name (`PollsIndexResponse`) and say that wrappers are named after their controller and action. Add no breaking-change notes. Verify that the example's names match the generated modules.
- [ ] 3.5 Verify that `pdm run pytest` passes offline and that `pdm run ruff check` on the new and changed test files is clean.

## 4. Final checks

- [ ] 4.1 Run `openspec validate type-inline-returns-objects --strict` and verify it passes.

## Workflow follow-up

- Commit the client after the fork commit (task 1.5). Coordinate the regeneration order with `generalize-union-property-types`.
- Archive with `/opsx:archive` after review.
