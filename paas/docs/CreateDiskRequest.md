# CreateDiskRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**size** | **str** |  | 

## Example

```python
from openapi_client.models.create_disk_request import CreateDiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiskRequest from a JSON string
create_disk_request_instance = CreateDiskRequest.from_json(json)
# print the JSON string representation of the object
print CreateDiskRequest.to_json()

# convert the object into a dict
create_disk_request_dict = create_disk_request_instance.to_dict()
# create an instance of CreateDiskRequest from a dict
create_disk_request_form_dict = create_disk_request.from_dict(create_disk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


