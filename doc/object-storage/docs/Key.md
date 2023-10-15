# Key


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**buckets** | [**List[KeyBucketsInner]**](KeyBucketsInner.md) |  | [optional] 
**status** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.key import Key

# TODO update the JSON string below
json = "{}"
# create an instance of Key from a JSON string
key_instance = Key.from_json(json)
# print the JSON string representation of the object
print Key.to_json()

# convert the object into a dict
key_dict = key_instance.to_dict()
# create an instance of Key from a dict
key_form_dict = key.from_dict(key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


