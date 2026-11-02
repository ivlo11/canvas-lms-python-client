# Tasks

## 1. Seed student and second admin tokens (canvas-lms fork, uncommitted)

- [x] 1.1 Re-read `spec/manual_seeding/large_gradebook_seeds.rb`, since the peer session may have changed it. Add `ensure_dev_token`, `ensure_second_admin` and `seed_role_tokens`, the `--tokens` and `--student-id` options, and the standalone branch (design D1–D5), as additive edits only. Verify that `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --help` in the web container lists both options and that `--observee-states` is still listed.
- [x] 1.2 Run `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --tokens` in the web container. Verify:
  - It prints the D5 summary.
  - `GET /api/v1/users/self` with the student token returns the chosen student, and `GET /api/v1/users/self/courses` returns at least one course.
  - `GET /api/v1/users/self` with the second admin token returns "Seeded Admin 2", and `GET /api/v1/accounts/self/admins` with `CANVAS_ADMIN_API_TOKEN` lists both admins.

  Record the chosen student's id (and whether it is the `CANVAS_API_TOKEN` observee) in these notes. Do not record the tokens.

  Notes: the default pick is student 8 ("Jessie 2"), enrolled in course 2. It is *not* the `CANVAS_API_TOKEN` observee, which is 168 ("Lizalfos 2"); student 8 is the observee of an older parent link. The second admin is user 392. `GET /api/v1/accounts/self/admins` lists users 1 and 392, both `AccountAdmin`.
- [x] 1.3 Run `--tokens` again. Verify that it prints the same tokens, that the student and admin each still have exactly one token with their purpose (rails runner count), and that there is still exactly one "Seeded Admin 2" and one account membership.
- [x] 1.4 Run `bin/rubocop spec/manual_seeding/large_gradebook_seeds.rb` and verify that it introduces no new offense types beyond the script's existing `Rails/Output` pattern. Verify with `git status` that the script is still uncommitted. Do not commit it.

  Notes: offense types are `Rails/Output`, `Rails/Exit`, `Rails/FindEach`, `Style/KeywordParametersOrder`, `Style/OptionalBooleanParameter` and `Lint/UnusedBlockArgument`. All of them were in the script before; the new code adds only `Rails/Output` and `Rails/Exit` (`exit`/`abort`, like the existing `--observee-states` branch).

## 2. Deliver

- [x] 2.1 Report to the user:
  - the student's name and id, and the second admin's name, id and login
  - both tokens, with the `export CANVAS_STUDENT_API_TOKEN=...` / `export CANVAS_SECOND_ADMIN_API_TOKEN=...` lines

  Verify that the tokens appear only in that report, and in no file under `openspec/` or either repo.

## Workflow follow-up

- A later change can add `CANVAS_STUDENT_API_TOKEN` / `CANVAS_SECOND_ADMIN_API_TOKEN` fixtures and README rows when a test needs them.
- Archive with `/opsx:archive` after review.
