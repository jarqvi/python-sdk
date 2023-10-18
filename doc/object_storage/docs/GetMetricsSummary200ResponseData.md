# GetMetricsSummary200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional] 
**metrics** | [**GetMetricsSummary200ResponseDataMetrics**](GetMetricsSummary200ResponseDataMetrics.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_metrics_summary200_response_data import GetMetricsSummary200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsSummary200ResponseData from a JSON string
get_metrics_summary200_response_data_instance = GetMetricsSummary200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetMetricsSummary200ResponseData.to_json()

# convert the object into a dict
get_metrics_summary200_response_data_dict = get_metrics_summary200_response_data_instance.to_dict()
# create an instance of GetMetricsSummary200ResponseData from a dict
get_metrics_summary200_response_data_form_dict = get_metrics_summary200_response_data.from_dict(get_metrics_summary200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


