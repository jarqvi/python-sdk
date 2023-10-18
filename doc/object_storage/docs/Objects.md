# Objects


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**ObjectsData**](ObjectsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.objects import Objects

# TODO update the JSON string below
json = "{}"
# create an instance of Objects from a JSON string
objects_instance = Objects.from_json(json)
# print the JSON string representation of the object
print Objects.to_json()

# convert the object into a dict
objects_dict = objects_instance.to_dict()
# create an instance of Objects from a dict
objects_form_dict = objects.from_dict(objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


