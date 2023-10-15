# GetDatabaseSummaryReports200ResponseCpuUsageInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GetDatabaseSummaryReports200ResponseCpuUsageInnerValueInner]**](GetDatabaseSummaryReports200ResponseCpuUsageInnerValueInner.md) |  | [optional] 
**applet** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_database_summary_reports200_response_cpu_usage_inner import GetDatabaseSummaryReports200ResponseCpuUsageInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabaseSummaryReports200ResponseCpuUsageInner from a JSON string
get_database_summary_reports200_response_cpu_usage_inner_instance = GetDatabaseSummaryReports200ResponseCpuUsageInner.from_json(json)
# print the JSON string representation of the object
print GetDatabaseSummaryReports200ResponseCpuUsageInner.to_json()

# convert the object into a dict
get_database_summary_reports200_response_cpu_usage_inner_dict = get_database_summary_reports200_response_cpu_usage_inner_instance.to_dict()
# create an instance of GetDatabaseSummaryReports200ResponseCpuUsageInner from a dict
get_database_summary_reports200_response_cpu_usage_inner_form_dict = get_database_summary_reports200_response_cpu_usage_inner.from_dict(get_database_summary_reports200_response_cpu_usage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


