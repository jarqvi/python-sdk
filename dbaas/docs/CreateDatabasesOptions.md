# CreateDatabasesOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standalone_replica_set** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.create_databases_options import CreateDatabasesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabasesOptions from a JSON string
create_databases_options_instance = CreateDatabasesOptions.from_json(json)
# print the JSON string representation of the object
print CreateDatabasesOptions.to_json()

# convert the object into a dict
create_databases_options_dict = create_databases_options_instance.to_dict()
# create an instance of CreateDatabasesOptions from a dict
create_databases_options_form_dict = create_databases_options.from_dict(create_databases_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


