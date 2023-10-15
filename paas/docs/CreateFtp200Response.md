# CreateFtp200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**host** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_ftp200_response import CreateFtp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFtp200Response from a JSON string
create_ftp200_response_instance = CreateFtp200Response.from_json(json)
# print the JSON string representation of the object
print CreateFtp200Response.to_json()

# convert the object into a dict
create_ftp200_response_dict = create_ftp200_response_instance.to_dict()
# create an instance of CreateFtp200Response from a dict
create_ftp200_response_form_dict = create_ftp200_response.from_dict(create_ftp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


