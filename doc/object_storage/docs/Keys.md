# Keys


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**keys** | [**List[Key]**](Key.md) |  | [optional] 

## Example

```python
from openapi_client.models.keys import Keys

# TODO update the JSON string below
json = "{}"
# create an instance of Keys from a JSON string
keys_instance = Keys.from_json(json)
# print the JSON string representation of the object
print Keys.to_json()

# convert the object into a dict
keys_dict = keys_instance.to_dict()
# create an instance of Keys from a dict
keys_form_dict = keys.from_dict(keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


