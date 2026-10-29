# AppointmentGroupsCreateRequestAppointmentGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_codes** | **str** | [] [Required, String] Array of context codes (courses, e.g. course_1) this group should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for this appointment group. | [optional] 
**sub_context_codes** | **str** | [] [String] Array of sub context codes (course sections or a single group category) this group should be linked to. Used to limit the appointment group to particular sections. If a group category is specified, students will sign up in groups and the participant_type will be \&quot;Group\&quot; instead of \&quot;User\&quot;. | [optional] 
**title** | **str** | [Required, String] Short title for the appointment group. | 
**description** | **str** | [String] Longer text description of the appointment group. | [optional] 
**location_name** | **str** | [String] Location name of the appointment group. | [optional] 
**location_address** | **str** | [String] Location address. | [optional] 
**publish** | **bool** | [Boolean] Indicates whether this appointment group should be published (i.e. made available for signup). Once published, an appointment group cannot be unpublished. Defaults to false. | [optional] 
**participants_per_appointment** | **int** | [Integer] Maximum number of participants that may register for each time slot. Defaults to null (no limit). | [optional] 
**min_appointments_per_participant** | **int** | [Integer] Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots. | [optional] 
**max_appointments_per_participant** | **int** | [Integer] Maximum number of time slots a user may register for. | [optional] 
**new_appointments** | **str** | [X][] Nested array of start time/end time pairs indicating time slots for this appointment group. Refer to the example request. | [optional] 
**participant_visibility** | **str** | [\&quot;private\&quot;|\&quot;protected\&quot;] \&quot;private\&quot;:: participants cannot see who has signed up for a particular             time slot \&quot;protected\&quot;:: participants can see who has signed up.  Defaults to               \&quot;private\&quot;. | [optional] 
**allow_observer_signup** | **bool** | [Boolean] Whether observer users can sign-up for an appointment. Defaults to false. | [optional] 

## Example

```python
from canvas_lms_python_client.models.appointment_groups_create_request_appointment_group import AppointmentGroupsCreateRequestAppointmentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentGroupsCreateRequestAppointmentGroup from a JSON string
appointment_groups_create_request_appointment_group_instance = AppointmentGroupsCreateRequestAppointmentGroup.from_json(json)
# print the JSON string representation of the object
print(AppointmentGroupsCreateRequestAppointmentGroup.to_json())

# convert the object into a dict
appointment_groups_create_request_appointment_group_dict = appointment_groups_create_request_appointment_group_instance.to_dict()
# create an instance of AppointmentGroupsCreateRequestAppointmentGroup from a dict
appointment_groups_create_request_appointment_group_from_dict = AppointmentGroupsCreateRequestAppointmentGroup.from_dict(appointment_groups_create_request_appointment_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


