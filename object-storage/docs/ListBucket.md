# ListBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_bucket import ListBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ListBucket from a JSON string
list_bucket_instance = ListBucket.from_json(json)
# print the JSON string representation of the object
print ListBucket.to_json()

# convert the object into a dict
list_bucket_dict = list_bucket_instance.to_dict()
# create an instance of ListBucket from a dict
list_bucket_form_dict = list_bucket.from_dict(list_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


