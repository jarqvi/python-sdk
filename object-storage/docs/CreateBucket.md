# CreateBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_bucket import CreateBucket

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBucket from a JSON string
create_bucket_instance = CreateBucket.from_json(json)
# print the JSON string representation of the object
print CreateBucket.to_json()

# convert the object into a dict
create_bucket_dict = create_bucket_instance.to_dict()
# create an instance of CreateBucket from a dict
create_bucket_form_dict = create_bucket.from_dict(create_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


