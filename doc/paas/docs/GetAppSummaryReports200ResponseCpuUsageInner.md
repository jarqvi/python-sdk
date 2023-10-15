# GetAppSummaryReports200ResponseCpuUsageInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GetAppSummaryReports200ResponseCpuUsageInnerValueInner]**](GetAppSummaryReports200ResponseCpuUsageInnerValueInner.md) |  | [optional] 
**applet** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_app_summary_reports200_response_cpu_usage_inner import GetAppSummaryReports200ResponseCpuUsageInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppSummaryReports200ResponseCpuUsageInner from a JSON string
get_app_summary_reports200_response_cpu_usage_inner_instance = GetAppSummaryReports200ResponseCpuUsageInner.from_json(json)
# print the JSON string representation of the object
print GetAppSummaryReports200ResponseCpuUsageInner.to_json()

# convert the object into a dict
get_app_summary_reports200_response_cpu_usage_inner_dict = get_app_summary_reports200_response_cpu_usage_inner_instance.to_dict()
# create an instance of GetAppSummaryReports200ResponseCpuUsageInner from a dict
get_app_summary_reports200_response_cpu_usage_inner_form_dict = get_app_summary_reports200_response_cpu_usage_inner.from_dict(get_app_summary_reports200_response_cpu_usage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


