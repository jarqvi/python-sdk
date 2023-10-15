# CreateKey201ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_key201_response_data import CreateKey201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKey201ResponseData from a JSON string
create_key201_response_data_instance = CreateKey201ResponseData.from_json(json)
# print the JSON string representation of the object
print CreateKey201ResponseData.to_json()

# convert the object into a dict
create_key201_response_data_dict = create_key201_response_data_instance.to_dict()
# create an instance of CreateKey201ResponseData from a dict
create_key201_response_data_form_dict = create_key201_response_data.from_dict(create_key201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


