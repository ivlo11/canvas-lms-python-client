# Tasks

## 1. Generator (canvas-lms fork)

- [x] 1.1 Copy the current `public/doc/openapi/canvas.openapi.yaml` to the scratchpad as the baseline. Verify that the copy exists.
- [x] 1.2 Add failing examples to `spec/lib/swagger_yard/canvas_adapter_spec.rb` for query parameter naming (design D1):
  - `include[]` → `include[]`
  - `placements` with an `Array` type → `placements[]`
  - `per_page` (Integer) → `per_page`
  - a path parameter and a body array parameter keep their names

  Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that only the new examples fail.
- [x] 1.3 Implement D1 in `add_query_parameter`. Verify that the 1.2 examples pass and that `bin/rspec spec/lib/swagger_yard/` passes.
- [x] 1.4 Regenerate the spec (`bundle exec rake doc:openapi`) and diff it against the 1.1 baseline. Verify that:
  - every array query parameter is named `…[]` (218 or more)
  - no scalar, path or body parameter changed
  - no operation has both `x` and `x[]`
  - responses and schemas are unchanged
- [x] 1.5 Run `bin/rubocop` on the generator and its spec. Verify that there are no new offenses compared with HEAD.
- [x] 1.6 Commit in the fork following its commit guidelines (generator and spec). Verify with `git log -1 --stat`.

## 2. Client (canvas-lms-python-client)

- [x] 2.1 Regenerate the client. Verify that every `_query_params.append` for an array parameter uses the `[]` name, and that no public method's parameter names changed (compare `inspect.signature` names across all API methods before and after; design D2).
- [x] 2.2 Add an offline test that builds a request for `lti_apps_launch_definitions` with two placements (for example via `_lti_apps_launch_definitions_serialize`) and asserts the URL query is `placements[]=…&placements[]=…`, and that `per_page` stays unbracketed. Add it to `src/.openapi-generator-ignore` and the README custom-files list. Verify that it passes.
- [x] 2.3 Run `pdm run pytest --integration -m integration -v`. Verify that `test_course_launch_definitions_yield_items` and `test_account_launch_definitions_yield_items` pass, not skip, against the seeded instance (the `resolve-namespaced-model-returns` seed has a `course_navigation` tool in course 8). Add a check that an `include[]` filter takes effect, for example `accounts_courses_api_all(include=["term"])` returns courses with `term` set.
- [x] 2.4 Add a README note: list query parameters are now sent as `name[]`, so filters that Canvas used to ignore now apply. Verify that `pdm run pytest` and `pdm run ruff check` pass on the new and changed test files.

## 3. Final checks

- [x] 3.1 Run `openspec validate fix-array-query-params --strict` and verify it passes.

## Workflow follow-up

- Commit the client after the fork commit (task 1.6).
- Archive with `/opsx:archive` after review.
