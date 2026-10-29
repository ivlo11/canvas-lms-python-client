# SisImportsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | Choose the data format for reading SIS data. With a standard Canvas install, this option can only be &#39;instructure_csv&#39;, and if unprovided, will be assumed to be so. Can be part of the query string. | [optional] 
**attachment** | **str** | There are three ways to post SIS import data: 1. As a multipart/form-data form field named +attachment+ 2. As a raw post with a Content-Type of application/zip or application/octet-stream 3. Using the {file:file.file_uploads.html File Upload} process, which can be more reliable    for large files. Use the +pre_attachment[name]+ argument to start that flow. See that    parameter below for more information.  +attachment+ is required for multipart/form-data style posts. Assumed to be SIS data from a file upload form field named +attachment+.  Examples:   curl -F attachment&#x3D;@&lt;filename&gt; -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports.json?import_type&#x3D;instructure_csv  If you decide to do a raw post, you can skip the &#39;attachment&#39; argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the &#39;extension&#39; argument.  Examples:   curl -H &#39;Content-Type: application/octet-stream&#39; --data-binary @&lt;filename&gt;.zip \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports.json?import_type&#x3D;instructure_csv&amp;extension&#x3D;zip    curl -H &#39;Content-Type: application/zip&#39; --data-binary @&lt;filename&gt;.zip \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports.json?import_type&#x3D;instructure_csv    curl -H &#39;Content-Type: text/csv&#39; --data-binary @&lt;filename&gt;.csv \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports.json?import_type&#x3D;instructure_csv    curl -H &#39;Content-Type: text/csv&#39; --data-binary @&lt;filename&gt;.csv \\       -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\       https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/sis_imports.json?import_type&#x3D;instructure_csv&amp;batch_mode&#x3D;1&amp;batch_mode_term_id&#x3D;15  If the attachment is a zip file, the uncompressed file(s) cannot be 100x larger than the zip, or the import will fail. For example, if the zip file is 1KB but the total size of the uncompressed file(s) is 100KB or greater the import will fail. There is a hard cap of 50 GB. | [optional] 
**extension** | **str** | Recommended for raw post request style imports. This field will be used to distinguish between zip, xml, csv, and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to zip-file format if all else fails. | [optional] 
**batch_mode** | **bool** | If set, this SIS import will be run in batch mode, deleting any data previously imported via SIS that is not present in this latest import. See the SIS CSV Format page for details. Batch mode cannot be used with diffing. | [optional] 
**batch_mode_term_id** | **str** | Limit deletions to only this term. Required if batch mode is enabled. | [optional] 
**multi_term_batch_mode** | **bool** | Runs batch mode against all terms in terms file. Requires change_threshold. | [optional] 
**skip_deletes** | **bool** | When set the import will skip any deletes. This does not account for objects that are deleted during the batch mode cleanup process. | [optional] 
**override_sis_stickiness** | **bool** | Default is false. If true, any fields containing “sticky” or UI changes will be overridden. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 
**add_sis_stickiness** | **bool** | This option, if present, will process all changes as if they were UI changes. This means that \&quot;stickiness\&quot; will be added to changed fields. This option is only processed if &#39;override_sis_stickiness&#39; is also provided. | [optional] 
**clear_sis_stickiness** | **bool** | This option, if present, will clear \&quot;stickiness\&quot; from all fields processed by this import. Requires that &#39;override_sis_stickiness&#39; is also provided. If &#39;add_sis_stickiness&#39; is also provided, &#39;clear_sis_stickiness&#39; will overrule the behavior of &#39;add_sis_stickiness&#39; | [optional] 
**update_sis_id_if_login_claimed** | **bool** | This option, if present, will override the old (or non-existent) non-matching SIS ID with the new SIS ID in the upload, if a pseudonym is found from the login field and the SIS ID doesn&#39;t match. | [optional] 
**diffing_data_set_identifier** | **str** | If set on a CSV import, Canvas will attempt to optimize the SIS import by comparing this set of CSVs to the previous set that has the same data set identifier, and only applying the difference between the two. See the SIS CSV Format documentation for more details. Diffing cannot be used with batch_mode | [optional] 
**diffing_remaster_data_set** | **bool** | If true, and diffing_data_set_identifier is sent, this SIS import will be part of the data set, but diffing will not be performed. See the SIS CSV Format documentation for details. | [optional] 
**diffing_drop_status** | **str** | If diffing_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. Defaults to &#39;deleted&#39; | [optional] 
**diffing_user_remove_status** | **str** | For users removed from one batch to the next one using the same diffing_data_set_identifier, set their status to the value of this argument. Defaults to &#39;deleted&#39;. | [optional] 
**batch_mode_enrollment_drop_status** | **str** | If batch_mode_enrollment_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. This will have an effect if multi_term_batch_mode is set. Defaults to &#39;deleted&#39; This will still mark courses and sections that are not included in the sis_batch as deleted, and subsequently enrollments in the deleted courses and sections as deleted. | [optional] 
**change_threshold** | **int** | If set with batch_mode, the batch cleanup process will not run if the number of items deleted is higher than the percentage set. If set to 10 and a term has 200 enrollments, and batch would delete more than 20 of the enrollments the batch will abort before the enrollments are deleted. The change_threshold will be evaluated for course, sections, and enrollments independently. If set with diffing, diffing will not be performed if the files are greater than the threshold as a percent. If set to 5 and the file is more than 5% smaller or more than 5% larger than the file that is being compared to, diffing will not be performed. If the files are less than 5%, diffing will be performed. The way the percent is calculated is by taking the size of the current import and dividing it by the size of the previous import. The formula used is: |(1 - current_file_size / previous_file_size)| * 100 See the SIS CSV Format documentation for more details. Required for multi_term_batch_mode. | [optional] 
**diff_row_count_threshold** | **int** | If set with diffing, diffing will not be performed if the number of rows to be run in the fully calculated diff import exceeds the threshold. | [optional] 
**pre_attachment** | [**SisImportsApiCreateRequestPreAttachment**](SisImportsApiCreateRequestPreAttachment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_imports_api_create_request import SisImportsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportsApiCreateRequest from a JSON string
sis_imports_api_create_request_instance = SisImportsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SisImportsApiCreateRequest.to_json())

# convert the object into a dict
sis_imports_api_create_request_dict = sis_imports_api_create_request_instance.to_dict()
# create an instance of SisImportsApiCreateRequest from a dict
sis_imports_api_create_request_from_dict = SisImportsApiCreateRequest.from_dict(sis_imports_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


