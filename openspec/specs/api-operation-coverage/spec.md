# api-operation-coverage Specification

## Purpose
Defines that the client exposes every documented, routed Canvas API endpoint under the name of the controller that documents it, so helper classes defined inside a controller can never rename, retype or hide that controller's endpoints.

## Requirements

### Requirement: Every documented routed endpoint is exposed
For every Canvas controller action that is documented as an API endpoint and has at least one route, the client SHALL provide an operation for each of that action's routes.

#### Scenario: Endpoints after a nested helper class
- **GIVEN** a controller that defines a nested helper class between its documented actions, such as the users controller's service-credentials struct
- **WHEN** the client is generated
- **THEN** the documented actions defined after the nested class, such as "Show user details", "Create a user" and "Edit a user", are available as client operations

#### Scenario: Nested helper class before every endpoint
- **GIVEN** a controller whose nested helper class is defined before all of its documented actions, such as the external tools controller
- **WHEN** the client is generated
- **THEN** all of that controller's documented actions are available as client operations

### Requirement: Operations are named after their own controller
Each client operation and its API class SHALL be named after the controller that documents the action, never after a class defined inside that controller.

#### Scenario: Users endpoints carry the users name
- **WHEN** the client is generated
- **THEN** "List users in account" is the `users_api_index` operation of the users API class
- **AND** no API class or operation is named after `ServiceCredentials`, `BadPermissionSettingError`, `RecordAlreadyExists` or `MetadataSaxDoc`

#### Scenario: Files endpoints are unchanged
- **GIVEN** the files controller, which defines a nested SAX document class
- **WHEN** the client is generated
- **THEN** the files API class and its operations have the same names and response types as before this change, and no additional operations

#### Scenario: Namespaced controllers are unaffected
- **GIVEN** a controller declared inside a module, such as an LTI controller
- **WHEN** the client is generated
- **THEN** its API class and operations have the same names as before this change

### Requirement: Nested helper classes do not alter response types
A documented response model of a controller action SHALL be reflected in the client's return type, regardless of any class defined inside that controller.

#### Scenario: Users list is typed
- **GIVEN** "List users in account", whose documentation returns a list of users
- **WHEN** users are listed with the page iterator
- **THEN** each page is a list of user models

#### Scenario: Roles list is typed
- **GIVEN** "List roles", whose documentation returns a list of roles
- **WHEN** roles are listed with the page iterator
- **THEN** each page is a list of role models

### Requirement: Only previously misnamed or hidden operations change
Regenerating the client with this behavior SHALL leave every other operation's name and response type unchanged.

#### Scenario: Operation set comparison
- **GIVEN** the operation identifiers and response types of the spec before and after this change
- **WHEN** they are compared
- **THEN** every removed identifier is one of the misnamed operations, and its renamed counterpart is present
- **AND** every added identifier belongs to one of the controllers that defined a nested helper class
- **AND** every operation present in both has the same response type, except for the misnamed operations whose documented model is restored
