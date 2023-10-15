# ResizeDatabaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **bool** |  | [optional] 
**plan_id** | **str** |  | 

## Example

```python
from openapi_client.models.resize_database_request import ResizeDatabaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResizeDatabaseRequest from a JSON string
resize_database_request_instance = ResizeDatabaseRequest.from_json(json)
# print the JSON string representation of the object
print ResizeDatabaseRequest.to_json()

# convert the object into a dict
resize_database_request_dict = resize_database_request_instance.to_dict()
# create an instance of ResizeDatabaseRequest from a dict
resize_database_request_form_dict = resize_database_request.from_dict(resize_database_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


