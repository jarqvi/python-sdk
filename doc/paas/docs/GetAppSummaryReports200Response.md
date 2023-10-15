# GetAppSummaryReports200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_usage** | [**List[GetAppSummaryReports200ResponseCpuUsageInner]**](GetAppSummaryReports200ResponseCpuUsageInner.md) |  | [optional] 
**memory_usage** | [**List[GetAppSummaryReports200ResponseCpuUsageInner]**](GetAppSummaryReports200ResponseCpuUsageInner.md) |  | [optional] 
**disks_usage** | [**List[GetAppSummaryReports200ResponseDisksUsageInner]**](GetAppSummaryReports200ResponseDisksUsageInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_app_summary_reports200_response import GetAppSummaryReports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppSummaryReports200Response from a JSON string
get_app_summary_reports200_response_instance = GetAppSummaryReports200Response.from_json(json)
# print the JSON string representation of the object
print GetAppSummaryReports200Response.to_json()

# convert the object into a dict
get_app_summary_reports200_response_dict = get_app_summary_reports200_response_instance.to_dict()
# create an instance of GetAppSummaryReports200Response from a dict
get_app_summary_reports200_response_form_dict = get_app_summary_reports200_response.from_dict(get_app_summary_reports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


