# Spec Delta

## REMOVED Requirements

### Requirement: Wrapped list responses yield typed wrapper pages
**Reason**: Related operations no longer share one wrapper model. Each wrapper is named after its controller and action, and wrappers can also come from an inline documented response.
**Migration**: Replaced by "Wrapped list responses yield per-action wrapper pages". The client is unreleased, so there are no consumers to migrate.

## ADDED Requirements

### Requirement: Wrapped list responses yield per-action wrapper pages
For each paginated operation whose Canvas documentation describes the response as an object wrapping a list of an existing model, in its example response or inline in its documented response, the page iterator SHALL yield one wrapper model per page, named after the operation's controller and action, with the list deserialized as the item model, across all result pages. A wrapper key SHALL be required only if Canvas documents it as required.

#### Scenario: Polls are returned in typed wrapper pages
- **GIVEN** the caller can see at least one poll
- **WHEN** polls are listed with the page iterator
- **THEN** each yielded page is a `PollsIndexResponse` wrapper model whose `polls` attribute is a list of poll models

#### Scenario: Related operations have their own wrappers
- **WHEN** poll sessions are listed for a poll, as opened sessions, or as closed sessions with the page iterator
- **THEN** each operation yields its own wrapper model type (`PollSessionsIndexResponse`, `PollSessionsOpenedResponse`, `PollSessionsClosedResponse`), and each has a `poll_sessions` attribute that is a list of poll session models

#### Scenario: Account calendars are returned in typed wrapper pages
- **GIVEN** the caller can see at least one account calendar
- **WHEN** account calendars are listed with the page iterator
- **THEN** each yielded page is a wrapper model whose `account_calendars` attribute is a list of account calendar models and whose `total_results` is an integer
- **AND** no all-items iterator is provided for the operation

#### Scenario: Wrapper key absent from a page
- **GIVEN** a page response for a wrapped operation that omits the wrapper key
- **WHEN** the page is deserialized
- **THEN** the page is yielded as a wrapper model whose wrapper attribute is empty, and no validation error is raised

#### Scenario: Wrapped results span multiple pages
- **GIVEN** a wrapped operation whose results span more than one page
- **WHEN** it is listed with the page iterator and a page size smaller than the total
- **THEN** one wrapper is yielded per page, following the `Link` next relation until there is none

#### Scenario: Undocumentable wrappers stay untyped
- **GIVEN** a wrapped operation that documents no response of its own, and whose example names a model that does not exist or is not a single key mapped to a list of a model
- **WHEN** the client is generated
- **THEN** that operation has no response type and remains on the undocumented allowlist
