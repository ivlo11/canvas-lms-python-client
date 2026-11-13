# OutcomeRollupLinksCourse

If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.outcome_rollup_links_course import OutcomeRollupLinksCourse

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeRollupLinksCourse from a JSON string
outcome_rollup_links_course_instance = OutcomeRollupLinksCourse.from_json(json)
# print the JSON string representation of the object
print(OutcomeRollupLinksCourse.to_json())

# convert the object into a dict
outcome_rollup_links_course_dict = outcome_rollup_links_course_instance.to_dict()
# create an instance of OutcomeRollupLinksCourse from a dict
outcome_rollup_links_course_from_dict = OutcomeRollupLinksCourse.from_dict(outcome_rollup_links_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


