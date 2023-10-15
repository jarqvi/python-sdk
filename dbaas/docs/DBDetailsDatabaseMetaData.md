# DBDetailsDatabaseMetaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standalone_replica_set** | **bool** | Indicates if the database uses a standalone replica set | [optional] 
**private_network** | **bool** | Indicates if the database is on a private network | [optional] 

## Example

```python
from openapi_client.models.db_details_database_meta_data import DBDetailsDatabaseMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of DBDetailsDatabaseMetaData from a JSON string
db_details_database_meta_data_instance = DBDetailsDatabaseMetaData.from_json(json)
# print the JSON string representation of the object
print DBDetailsDatabaseMetaData.to_json()

# convert the object into a dict
db_details_database_meta_data_dict = db_details_database_meta_data_instance.to_dict()
# create an instance of DBDetailsDatabaseMetaData from a dict
db_details_database_meta_data_form_dict = db_details_database_meta_data.from_dict(db_details_database_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


