# StatDataObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **float** |  | [optional] 
**meta_data** | [**StatDataObjectMetaData**](StatDataObjectMetaData.md) |  | [optional] 
**last_modified** | **str** |  | [optional] 
**version_id** | **str** |  | [optional] 
**etag** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stat_data_object import StatDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of StatDataObject from a JSON string
stat_data_object_instance = StatDataObject.from_json(json)
# print the JSON string representation of the object
print StatDataObject.to_json()

# convert the object into a dict
stat_data_object_dict = stat_data_object_instance.to_dict()
# create an instance of StatDataObject from a dict
stat_data_object_form_dict = stat_data_object.from_dict(stat_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


