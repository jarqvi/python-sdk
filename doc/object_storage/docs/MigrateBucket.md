# MigrateBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.migrate_bucket import MigrateBucket

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateBucket from a JSON string
migrate_bucket_instance = MigrateBucket.from_json(json)
# print the JSON string representation of the object
print MigrateBucket.to_json()

# convert the object into a dict
migrate_bucket_dict = migrate_bucket_instance.to_dict()
# create an instance of MigrateBucket from a dict
migrate_bucket_form_dict = migrate_bucket.from_dict(migrate_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


