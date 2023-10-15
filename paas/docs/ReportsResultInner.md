# ReportsResultInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[List[GetAppSummaryReports200ResponseCpuUsageInnerValueInner]]** |  | [optional] 
**applet** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.reports_result_inner import ReportsResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsResultInner from a JSON string
reports_result_inner_instance = ReportsResultInner.from_json(json)
# print the JSON string representation of the object
print ReportsResultInner.to_json()

# convert the object into a dict
reports_result_inner_dict = reports_result_inner_instance.to_dict()
# create an instance of ReportsResultInner from a dict
reports_result_inner_form_dict = reports_result_inner.from_dict(reports_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


