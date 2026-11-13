# Tasks

## 1. Generator and schema (canvas-lms fork)

- [x] 1.1 In `spec/lib/swagger_yard/canvas_adapter_spec.rb`'s `.resolve_schema_name` block, add failing examples: `"Schemas::Docs::User"` returns `"User"`, and `"Schemas::Docs::Missing"` returns nil. Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that only the new examples fail.

  Notes: 161 examples, 1 failure. The `Schemas::Docs::Missing` example already passes, because the unknown name resolves to nil either way.
- [x] 1.2 Implement D1 in `resolve_schema_name`. Verify that the 1.1 examples pass and that `bin/rspec spec/lib/swagger_yard/` passes as a whole.

  Notes: `name.to_s.delete_prefix("Schemas::Docs::")` before `sanitize_schema_name`. 161 examples, 0 failures.
- [x] 1.3 Add D2's `permissions`, `effective_locale` and `uuid` to `lib/schemas/docs/user.rb`. Verify that `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb lib/schemas/docs/user.rb` reports no new offenses.

  Notes: same offenses before and after (`Rails/Output` 1, `RSpec/BeforeAfterAll` 1, `RSpec/RepeatedDescription` 12).
- [x] 1.4 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and diff it with the previous spec. Verify:
  - `Users-api_show`'s 200 response is `$ref: User`.
  - `User` has the three new properties, and `permissions` has its three boolean properties. If it's a bare `object`, record that.
  - No other operation's response and no other schema changed.

  Notes: only `User` and `get /api/v1/users/{id}` changed. The response is `$ref: User` under `default` (every operation in the spec uses `default`, not `200`); its description reads `Schemas::Docs::User`, the raw tag text (cosmetic). `permissions` is a bare `type: object`: `convert_single_property` doesn't carry nested `properties` through, so the client types it `Dict[str, Any]`. The keys stay documented in `user.rb` for Canvas's HTML docs.
- [x] 1.5 Commit `canvas_adapter.rb`, its spec and `lib/schemas/docs/user.rb` in upstream format (D4). Verify that `git log -1 --stat` lists only those files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.

  Notes: committed as `fix(swagger_yard): resolve Schemas::Docs @returns`. The host `script/rlint` pre-commit step errors again without blocking.

## 2. Client (canvas-lms-python-client)

- [x] 2.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keeping existing `test_*.py` entries the generator drops). Verify:
  - `users_api_show` returns `User`.
  - `models/user.py` declares `permissions`, `effective_locale` and `uuid`.

  Notes: `users_api_show` and its variants return `User`. `docs/LtiRegistrationCreatedBy.md` also lists the 3 new fields (the `created_by` oneOf wrapper). `FILES` unchanged; no orphans.
- [x] 2.2 Capture `users_self.json` (D3) and add `test/custom/unit/test_user_model.py`. Verify that it passes, and that it fails against the pre-change `models/user.py`: check out the old file, confirm the failure, then restore it.

  Notes: the admin `self` payload is captured as Seeded Admin 2 (392), not user 1, whose name, login and email are a real address. Fixture order: observer 218, student 8, admin 392, admin 392 reading user 8 (no `effective_locale`). `permissions` is asserted as a dict (see 1.4). 5 passed; against the HEAD `models/user.py`, 4 failed.
- [x] 2.3 Add `test_users_api_show_self_is_typed` (D3), and switch `test_student_grades.py` to `student.id`. Verify with `pdm run pytest --integration -v -k "users_api_show or computed_grades"` (all three tokens set) that both pass.

  Notes: the test uses the observer client (`canvas_api_client`). Both pass.
- [x] 2.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client, staging only this change's files.

  Notes: offline 3722 passed, 161 skipped (+1: the new integration test). `--integration`: 19 passed, 6 skipped, the same seeded-data skips. ruff clean. Committed as `fix(canvas_lms_python_client): type show user details`.

## 3. Final checks

- [x] 3.1 Run `openspec validate type-show-user-details --strict` and verify that it passes.

## Workflow follow-up

- Document the other `user_json` keys `User` lacks: `created_at`, `account_uuid`, `past_uuid`, `confirmation_url`.
- Carry nested `properties` of object properties through `convert_single_property`, so `User.permissions` is typed.
- Use the resolved model name, not the raw `@returns` text, as the response description.
- Archive with `/opsx:archive` after review.
