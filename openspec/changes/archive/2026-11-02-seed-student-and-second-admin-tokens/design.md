# Design

## Context

- Motivation: see proposal.md, "Why". There are no spec deltas: this is seed tooling only.
- **How tokens work** (`app/models/access_token.rb`):
  - `AccessToken#token=` stores only `crypted_token = hashed_token(raw)` plus a 5-character hint.
  - `full_token` is available only on the instance that set it.
  - `generate_token` runs `before_create` only when no `crypted_token` is set.
  - So a token whose raw string the seed sets explicitly can be found again by `crypted_token: AccessToken.hashed_token(raw)` and printed again. A random token couldn't be.
- **The existing seed** (`spec/manual_seeding/large_gradebook_seeds.rb`):
  - Parents get `parent.access_tokens.build(token: "canvas_parent_dev_token_#{unique_id}", purpose: ...)`.
  - Pseudonyms use random 10-digit `unique_id`s with the password `password123`.
  - `ACCOUNT = Account.default` (the "demo-dashboard" account, id 1).
  - `--observee-states` shows the pattern for an option that runs on its own: a branch that runs one helper in a transaction and exits before the bulk creation.
- **Live instance:** account 1 has one `AccountAdmin`, user 1, which owns `CANVAS_ADMIN_API_TOKEN`. The observer token belongs to user 218 ("Parent of Lizalfos 2"), who observes student 168.

## Goals / Non-Goals

**Goals:**
- A working student token and a second admin with a working token, both reprintable on rerun.

**Non-Goals:**
- Wiring the tokens into client tests or the README (later).
- Rotating or expiring tokens, or developer keys and scopes. Like the parent tokens, these are plain user tokens with no developer key.

## Decisions

### D1: A standalone, idempotent `--tokens` option
Add `opts.on("--tokens", ...)` and a branch that runs `CreateHelpers.seed_role_tokens(student_id:)` in a transaction, prints the summary, and exits, as `--observee-states` does. `--student-id ID` sets `student_id`. It's valid only with `--tokens`, and is ignored otherwise.

### D2: Picking the student
- With `--student-id`: that user, who must have an active student enrollment on the default account. Otherwise the script aborts with a message.
- Otherwise: the student of the oldest active `UserObservationLink` on `ACCOUNT` (ordered by `id`). Today that's expected to be 168, the observee behind `CANVAS_API_TOKEN`. The apply step records the actual pick.
- *Alternative: create a new student.* A new student would have no courses, submissions or observer, which would make the token much less useful.

### D3: Fixed token strings, found or created
`ensure_dev_token(user, raw:, purpose:)`:
- It returns the existing token found by `user.access_tokens.where(crypted_token: AccessToken.hashed_token(raw)).first`.
- Otherwise it builds one with `token: raw, purpose:` and saves it.
- It always returns `raw` for printing.

The raw strings are `canvas_student_dev_token_<user.id>` and `canvas_admin2_dev_token_<user.id>`.

These strings are guessable. That's acceptable only because this is a local, dummy-data instance and the script is never committed, which is the same trade-off the parent tokens already make. A comment in the helper says so.
- *Alternative: random tokens.* They couldn't be printed on a rerun, so each run would add another token.

### D4: Second admin
`ensure_second_admin`:
- Find the user by pseudonym `unique_id: "seeded_admin_2"` on `ACCOUNT`.
- Otherwise create `User` "Seeded Admin 2", `register!` it, and add a pseudonym (`seeded_admin_2`, password `password123`).
- Ensure `ACCOUNT.account_users.find_or_create_by!(user:, role: Role.get_built_in_role("AccountAdmin", root_account_id: ACCOUNT.id))` exists and is active.

The fixed login, rather than a random one like the parents', is what makes the lookup idempotent.

### D5: The printed summary
```
Student:        <name> (id <id>)   Token: <raw>
Second admin:   Seeded Admin 2 (id <id>)  Login: seeded_admin_2 / password123   Token: <raw>
export CANVAS_STUDENT_API_TOKEN="<raw>"
export CANVAS_SECOND_ADMIN_API_TOKEN="<raw>"
```
The apply step copies the student and admin ids and both tokens into its report to the user. It doesn't put them in these planning files, because tokens don't belong in docs under version control.

## Risks / Trade-offs

- [The peer session edits the same file at the same time] → Make additive edits only: new helpers and a new option branch. Re-read the file just before editing and run the script after both changes are in.
- [The predictable tokens leak beyond the dev box] → They work only against this local instance's database. The script is never committed, and the tokens are kept out of version-controlled docs.
- [`AccountAdmin` role lookup differs by Canvas version] → Use `Role.get_built_in_role`, as Canvas's own seeds do. If it fails, the task stops and records it.

## Migration Plan

1. Run with `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --tokens` in the web container.
2. Verify the tokens with `GET /api/v1/users/self`.
3. Report the tokens.

Rollback: delete the created tokens, account membership and user from a Rails console.
