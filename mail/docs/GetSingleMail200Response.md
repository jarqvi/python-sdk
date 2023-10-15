# GetSingleMail200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**GetSingleMail200ResponseData**](GetSingleMail200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_single_mail200_response import GetSingleMail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSingleMail200Response from a JSON string
get_single_mail200_response_instance = GetSingleMail200Response.from_json(json)
# print the JSON string representation of the object
print GetSingleMail200Response.to_json()

# convert the object into a dict
get_single_mail200_response_dict = get_single_mail200_response_instance.to_dict()
# create an instance of GetSingleMail200Response from a dict
get_single_mail200_response_form_dict = get_single_mail200_response.from_dict(get_single_mail200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


