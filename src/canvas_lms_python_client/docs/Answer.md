# Answer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the answer.  Do not supply if this answer is part of a new question | [optional] 
**answer_text** | **str** | The text of the answer. | 
**answer_weight** | **int** | An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100. | 
**answer_comments** | **str** | Specific contextual comments for a particular answer. | [optional] 
**text_after_answers** | **str** | Used in missing word questions.  The text to follow the missing word | [optional] 
**answer_match_left** | **str** | Used in matching questions.  The static value of the answer that will be displayed on the left for students to match for. | [optional] 
**answer_match_right** | **str** | Used in matching questions. The correct match for the value given in answer_match_left.  Will be displayed in a dropdown with the other answer_match_right values.. | [optional] 
**matching_answer_incorrect_matches** | **str** | Used in matching questions. A list of distractors, delimited by new lines ( ) that will be seeded with all the answer_match_right values. | [optional] 
**numerical_answer_type** | **str** | Used in numerical questions.  Values can be &#39;exact_answer&#39;, &#39;range_answer&#39;, or &#39;precision_answer&#39;. | [optional] 
**exact** | **int** | Used in numerical questions of type &#39;exact_answer&#39;.  The value the answer should equal. | [optional] 
**margin** | **int** | Used in numerical questions of type &#39;exact_answer&#39;. The margin of error allowed for the student&#39;s answer. | [optional] 
**approximate** | **float** | Used in numerical questions of type &#39;precision_answer&#39;.  The value the answer should equal. | [optional] 
**precision** | **int** | Used in numerical questions of type &#39;precision_answer&#39;. The numerical precision that will be used when comparing the student&#39;s answer. | [optional] 
**start** | **int** | Used in numerical questions of type &#39;range_answer&#39;. The start of the allowed range (inclusive). | [optional] 
**end** | **int** | Used in numerical questions of type &#39;range_answer&#39;. The end of the allowed range (inclusive). | [optional] 
**blank_id** | **int** | Used in fill in multiple blank and multiple dropdowns questions. | [optional] 
**html** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**comments_html** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.answer import Answer

# TODO update the JSON string below
json = "{}"
# create an instance of Answer from a JSON string
answer_instance = Answer.from_json(json)
# print the JSON string representation of the object
print(Answer.to_json())

# convert the object into a dict
answer_dict = answer_instance.to_dict()
# create an instance of Answer from a dict
answer_from_dict = Answer.from_dict(answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


