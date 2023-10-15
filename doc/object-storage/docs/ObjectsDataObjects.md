# ObjectsDataObjects


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_truncated** | **bool** |  | [optional] 
**contents** | [**List[ObjectsDataObjectsContentsInner]**](ObjectsDataObjectsContentsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**delimiter** | **str** |  | [optional] 
**max_keys** | **float** |  | [optional] 
**common_prefixes** | [**List[ObjectsDataObjectsCommonPrefixesInner]**](ObjectsDataObjectsCommonPrefixesInner.md) |  | [optional] 
**key_count** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.objects_data_objects import ObjectsDataObjects

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsDataObjects from a JSON string
objects_data_objects_instance = ObjectsDataObjects.from_json(json)
# print the JSON string representation of the object
print ObjectsDataObjects.to_json()

# convert the object into a dict
objects_data_objects_dict = objects_data_objects_instance.to_dict()
# create an instance of ObjectsDataObjects from a dict
objects_data_objects_form_dict = objects_data_objects.from_dict(objects_data_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


