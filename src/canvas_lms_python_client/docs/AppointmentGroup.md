# AppointmentGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the appointment group | [optional] 
**title** | **str** | The title of the appointment group | [optional] 
**start_at** | **datetime** | The start of the first time slot in the appointment group | [optional] 
**end_at** | **datetime** | The end of the last time slot in the appointment group | [optional] 
**description** | **str** | The text description of the appointment group | [optional] 
**location_name** | **str** | The location name of the appointment group | [optional] 
**location_address** | **str** | The address of the appointment group&#39;s location | [optional] 
**participant_count** | **int** | The number of participant who have reserved slots (see include[] argument) | [optional] 
**reserved_times** | [**List[Appointment]**](Appointment.md) | The start and end times of slots reserved by the current user as well as the id of the calendar event for the reservation (see include[] argument) | [optional] 
**allow_observer_signup** | **bool** | Boolean indicating whether observer users should be able to sign-up for an appointment | [optional] 
**context_codes** | **List[str]** | The context codes (i.e. courses) this appointment group belongs to. Only people in these courses will be eligible to sign up. | [optional] 
**sub_context_codes** | **List[int]** | The sub-context codes (i.e. course sections and group categories) this appointment group is restricted to | [optional] 
**workflow_state** | **str** | Current state of the appointment group (&#39;pending&#39;, &#39;active&#39; or &#39;deleted&#39;). &#39;pending&#39; indicates that it has not been published yet and is invisible to participants. | [optional] 
**requiring_action** | **bool** | Boolean indicating whether the current user needs to sign up for this appointment group (i.e. it&#39;s reservable and the min_appointments_per_participant limit has not been met by this user). | [optional] 
**appointments_count** | **int** | Number of time slots in this appointment group | [optional] 
**appointments** | [**List[CalendarEvent]**](CalendarEvent.md) | Calendar Events representing the time slots (see include[] argument) Refer to the Calendar Events API for more information | [optional] 
**new_appointments** | [**List[CalendarEvent]**](CalendarEvent.md) | Newly created time slots (same format as appointments above). Only returned in Create/Update responses where new time slots have been added | [optional] 
**max_appointments_per_participant** | **int** | Maximum number of time slots a user may register for, or null if no limit | [optional] 
**min_appointments_per_participant** | **int** | Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots | [optional] 
**participants_per_appointment** | **int** | Maximum number of participants that may register for each time slot, or null if no limit | [optional] 
**participant_visibility** | **str** | &#39;private&#39; means participants cannot see who has signed up for a particular time slot, &#39;protected&#39; means that they can | [optional] 
**participant_type** | **str** | Indicates how participants sign up for the appointment group, either as individuals (&#39;User&#39;) or in student groups (&#39;Group&#39;). Related to sub_context_codes (i.e. &#39;Group&#39; signups always have a single group category) | [optional] 
**url** | **str** | URL for this appointment group (to update, delete, etc.) | [optional] 
**html_url** | **str** | URL for a user to view this appointment group | [optional] 
**created_at** | **datetime** | When the appointment group was created | [optional] 
**updated_at** | **datetime** | When the appointment group was last updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.appointment_group import AppointmentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AppointmentGroup from a JSON string
appointment_group_instance = AppointmentGroup.from_json(json)
# print the JSON string representation of the object
print(AppointmentGroup.to_json())

# convert the object into a dict
appointment_group_dict = appointment_group_instance.to_dict()
# create an instance of AppointmentGroup from a dict
appointment_group_from_dict = AppointmentGroup.from_dict(appointment_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


