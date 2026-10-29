# ContentMigrationsCreateRequestDateShiftOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_dates** | **bool** | [Boolean] Whether to shift dates in the copied course | [optional] 
**old_start_date** | **str** | [Date] The original start date of the source content/course | [optional] 
**old_end_date** | **str** | [Date] The original end date of the source content/course | [optional] 
**new_start_date** | **str** | [Date] The new start date for the content/course | [optional] 
**new_end_date** | **str** | [Date] The new end date for the source content/course | [optional] 
**day_substitutions** | **str** | [X] [Integer] Move anything scheduled for day &#39;X&#39; to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday) | [optional] 
**remove_dates** | **bool** | [Boolean] Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_migrations_create_request_date_shift_options import ContentMigrationsCreateRequestDateShiftOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ContentMigrationsCreateRequestDateShiftOptions from a JSON string
content_migrations_create_request_date_shift_options_instance = ContentMigrationsCreateRequestDateShiftOptions.from_json(json)
# print the JSON string representation of the object
print(ContentMigrationsCreateRequestDateShiftOptions.to_json())

# convert the object into a dict
content_migrations_create_request_date_shift_options_dict = content_migrations_create_request_date_shift_options_instance.to_dict()
# create an instance of ContentMigrationsCreateRequestDateShiftOptions from a dict
content_migrations_create_request_date_shift_options_from_dict = ContentMigrationsCreateRequestDateShiftOptions.from_dict(content_migrations_create_request_date_shift_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


