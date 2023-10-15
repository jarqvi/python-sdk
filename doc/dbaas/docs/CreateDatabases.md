# CreateDatabases


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname of databases that you want to create | [optional] 
**options** | [**CreateDatabasesOptions**](CreateDatabasesOptions.md) |  | [optional] 
**public_network** | **bool** | The publicNetwork of databases that you want to create | [optional] 
**type** | **str** | The type of databases that you want to create | [optional] 
**plan_id** | **str** | The planID of databases that you want to create | [optional] 
**version** | **str** | The version of databases that you want to create | [optional] 

## Example

```python
from openapi_client.models.create_databases import CreateDatabases

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabases from a JSON string
create_databases_instance = CreateDatabases.from_json(json)
# print the JSON string representation of the object
print CreateDatabases.to_json()

# convert the object into a dict
create_databases_dict = create_databases_instance.to_dict()
# create an instance of CreateDatabases from a dict
create_databases_form_dict = create_databases.from_dict(create_databases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


