# Tasks

## 1. Generator (canvas-lms fork)

- [ ] 1.1 Copy the current `public/doc/openapi/canvas.openapi.yaml` to the scratchpad as the baseline. Verify that the copy exists.
- [ ] 1.2 Add examples to the `.convert_single_property` block in `spec/lib/swagger_yard/canvas_adapter_spec.rb` (canvas_schemas seeded with `User`, `Lti_A`, `Lti_B`):
  - `string|User` + `$ref User` → `oneOf [string, $ref User]` (passes today)
  - `integer|string` → `oneOf [integer, string]`, with description kept
  - `User|null` + `$ref User` → `$ref User` with `nullable`
  - `Lti::A|string` with no `$ref` → `oneOf [$ref Lti_A, string]`
  - `string|DateTime` → plain `string`
  - `Lti::A|Lti::B` → `$ref Lti_A`, plus a warning on stdout
  - `string|Missing` → `string`, plus a warning
  - bare `$ref`, `{"type" => "User", "$ref" => "User"}`, plain `string`, `["integer", "null"]` → unchanged output

  Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that only the new union examples fail.
- [ ] 1.3 Implement design D1–D4: extract `convert_scalar_property`, add the per-part variant helper, and replace the `string`-only check. Verify that the 1.2 examples pass and that `bin/rspec spec/lib/swagger_yard/` passes.
- [ ] 1.4 Regenerate the spec (`bundle exec rake doc:openapi`). Verify that it is identical to the 1.1 baseline (`cmp`), and that the run prints no new union warnings.
- [ ] 1.5 Run `bin/rubocop` on the generator and its spec. Verify that there are no new offenses compared with HEAD.
- [ ] 1.6 Commit in the fork following its commit guidelines (generator and spec). Verify with `git log -1 --stat`.

## 2. Client (canvas-lms-python-client)

- [ ] 2.1 Regenerate the client. Verify with `git status` that no generated file changed, and that `pdm run pytest` passes, including `test_lti_model_payloads.py`.

## 3. Final checks

- [ ] 3.1 Run `openspec validate generalize-union-property-types --strict` and verify it passes.

## Workflow follow-up

- Unions inside array `items`, and the two-type JSON array form, are follow-ups if Canvas docs start using them.
- Archive with `/opsx:archive` after review.
