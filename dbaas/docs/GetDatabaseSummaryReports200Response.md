# GetDatabaseSummaryReports200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_usage** | [**List[GetDatabaseSummaryReports200ResponseCpuUsageInner]**](GetDatabaseSummaryReports200ResponseCpuUsageInner.md) |  | [optional] 
**memory_usage** | [**List[GetDatabaseSummaryReports200ResponseCpuUsageInner]**](GetDatabaseSummaryReports200ResponseCpuUsageInner.md) |  | [optional] 
**disks_usage** | [**List[GetDatabaseSummaryReports200ResponseDisksUsageInner]**](GetDatabaseSummaryReports200ResponseDisksUsageInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_database_summary_reports200_response import GetDatabaseSummaryReports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabaseSummaryReports200Response from a JSON string
get_database_summary_reports200_response_instance = GetDatabaseSummaryReports200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabaseSummaryReports200Response.to_json()

# convert the object into a dict
get_database_summary_reports200_response_dict = get_database_summary_reports200_response_instance.to_dict()
# create an instance of GetDatabaseSummaryReports200Response from a dict
get_database_summary_reports200_response_form_dict = get_database_summary_reports200_response.from_dict(get_database_summary_reports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


