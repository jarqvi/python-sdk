# GetHisotricalMetrics200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**GetHisotricalMetrics200ResponseData**](GetHisotricalMetrics200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_hisotrical_metrics200_response import GetHisotricalMetrics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHisotricalMetrics200Response from a JSON string
get_hisotrical_metrics200_response_instance = GetHisotricalMetrics200Response.from_json(json)
# print the JSON string representation of the object
print GetHisotricalMetrics200Response.to_json()

# convert the object into a dict
get_hisotrical_metrics200_response_dict = get_hisotrical_metrics200_response_instance.to_dict()
# create an instance of GetHisotricalMetrics200Response from a dict
get_hisotrical_metrics200_response_form_dict = get_hisotrical_metrics200_response.from_dict(get_hisotrical_metrics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


