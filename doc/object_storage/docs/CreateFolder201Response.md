# CreateFolder201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**CreateFolder201ResponseData**](CreateFolder201ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_folder201_response import CreateFolder201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder201Response from a JSON string
create_folder201_response_instance = CreateFolder201Response.from_json(json)
# print the JSON string representation of the object
print CreateFolder201Response.to_json()

# convert the object into a dict
create_folder201_response_dict = create_folder201_response_instance.to_dict()
# create an instance of CreateFolder201Response from a dict
create_folder201_response_form_dict = create_folder201_response.from_dict(create_folder201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


