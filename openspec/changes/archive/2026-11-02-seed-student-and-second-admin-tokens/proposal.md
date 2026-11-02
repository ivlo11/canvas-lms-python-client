# Proposal

## Why

Integration tests can authenticate as only two roles today:
- an observer: `CANVAS_API_TOKEN`, from the seeded "Parent of …" users
- the one account admin: `CANVAS_ADMIN_API_TOKEN`, user 1, which wasn't created by the seed script

There's no seeded token for a student, so student-scoped endpoints such as a student's own submissions or what-if grades can't be exercised. There's also no second admin, so admin-to-admin cases (for example admin listings, or data owned by another admin) can't be tested either.

## What Changes

- **Seed script (canvas-lms fork, never committed):** a new `--tokens` option on `spec/manual_seeding/large_gradebook_seeds.rb` that runs on its own (like `--observee-states`) and is idempotent:
  - **Student token:** for one seeded student, create (or reuse) an access token. By default the student is the observee of the oldest active observer link, so student and observer tests see the same data. `--student-id <id>` picks a different student.
  - **Second admin:** create (or reuse) a registered user "Seeded Admin 2" with a login and password, make them an `AccountAdmin` on the default account, and create (or reuse) their access token.
  - Each token string is fixed in advance (`canvas_student_dev_token_<user id>`, `canvas_admin2_dev_token_<user id>`), following the existing parent tokens. A rerun therefore finds the same token and prints it again, instead of creating a new one.
  - The script prints a summary of the student and admin with their user ids, logins and tokens, plus `export` lines for `CANVAS_STUDENT_API_TOKEN` and `CANVAS_SECOND_ADMIN_API_TOKEN`.
- **Delivering the tokens:** after running the script, the apply step reports both tokens, with their user ids, to the user.
- **Not in scope:**
  - client test fixtures or README environment variables that use these tokens (a later change, when a test needs them)
  - changes to the existing observer or admin tokens

## Capabilities

### New Capabilities
<!-- None. Seed tooling only; no client behavior changes. -->

### Modified Capabilities
<!-- None. The change sets `skip_specs: true`. -->

## Impact

- **canvas-lms (fork):** `spec/manual_seeding/large_gradebook_seeds.rb` only, uncommitted, plus rows in the dev database: one user, a pseudonym, an account membership and two access tokens.
- **canvas-lms-python-client:** no code changes.
- **Concurrency:** `count-observee-submission-states` is editing the same seed script in another session (`--observee-states`). This change only adds new helpers and a new option.
