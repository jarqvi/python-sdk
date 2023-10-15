# KeyBucketsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.key_buckets_inner import KeyBucketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of KeyBucketsInner from a JSON string
key_buckets_inner_instance = KeyBucketsInner.from_json(json)
# print the JSON string representation of the object
print KeyBucketsInner.to_json()

# convert the object into a dict
key_buckets_inner_dict = key_buckets_inner_instance.to_dict()
# create an instance of KeyBucketsInner from a dict
key_buckets_inner_form_dict = key_buckets_inner.from_dict(key_buckets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


