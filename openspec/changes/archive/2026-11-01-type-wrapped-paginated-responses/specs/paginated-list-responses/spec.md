# Spec Delta

## ADDED Requirements

### Requirement: Wrapped list responses yield typed wrapper pages
For each paginated operation whose Canvas documentation describes the response as an object wrapping a list of an existing model under one key, the page iterator SHALL yield one wrapper model per page, with that key's items deserialized as the item model, across all result pages. A wrapper key SHALL be required only if Canvas documents it as required.

#### Scenario: Polls are returned in typed wrapper pages
- **GIVEN** the caller can see at least one poll
- **WHEN** polls are listed with the page iterator
- **THEN** each yielded page is a wrapper model whose `polls` attribute is a list of poll models

#### Scenario: Shared wrapper across related operations
- **WHEN** poll sessions are listed for a poll, as opened sessions, or as closed sessions with the page iterator
- **THEN** each yielded page is the same poll-sessions wrapper model type, whose `poll_sessions` attribute is a list of poll session models

#### Scenario: Wrapper key absent from a page
- **GIVEN** a page response for a wrapped operation that omits the wrapper key
- **WHEN** the page is deserialized
- **THEN** the page is yielded as a wrapper model whose wrapper attribute is empty, and no validation error is raised

#### Scenario: Wrapped results span multiple pages
- **GIVEN** a wrapped operation whose results span more than one page
- **WHEN** it is listed with the page iterator and a page size smaller than the total
- **THEN** one wrapper is yielded per page, following the `Link` next relation until there is none

#### Scenario: Undocumentable wrappers stay untyped
- **GIVEN** a wrapped operation whose example names a model that does not exist, or whose example is not a single key mapped to a list of a model
- **WHEN** the client is generated
- **THEN** that operation has no response type and remains on the undocumented allowlist

### Requirement: All-items iterator exists only for list responses
The client SHALL provide the all-items iterator for a paginated operation only when that operation's response is a list. The single-call method and the page iterator SHALL be provided for every paginated operation.

#### Scenario: List response
- **GIVEN** a paginated operation whose response is a list of a model
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method, the page iterator, and the all-items iterator for that operation

#### Scenario: Wrapper or object response
- **GIVEN** a paginated operation whose response is a wrapper model or an untyped object, such as polls or enrollment terms
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method and the page iterator, and does not provide an all-items iterator

#### Scenario: Undocumented response
- **GIVEN** a paginated operation with no documented response type
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method and the page iterator, and does not provide an all-items iterator
