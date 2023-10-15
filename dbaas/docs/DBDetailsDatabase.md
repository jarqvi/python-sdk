# DBDetailsDatabase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbid** | **str** | The ID of the database | [optional] 
**type** | **str** | The type of the database | [optional] 
**plan_id** | **str** | The plan ID | [optional] 
**status** | **str** | The status of the database | [optional] 
**scale** | **int** | The scale of the database | [optional] 
**hostname** | **str** | The hostname of the database | [optional] 
**public_network** | **bool** | Indicates if the database is on a public network | [optional] 
**version** | **str** | The database version | [optional] 
**volume_size** | **int** | The size of the database volume | [optional] 
**created_at** | **str** | The creation timestamp of the database | [optional] 
**db_name** | **str** | The name of db | [optional] 
**node** | [**DBDetailsDatabaseNode**](DBDetailsDatabaseNode.md) |  | [optional] 
**port** | **int** | The port number for the database connection | [optional] 
**root_password** | **str** | The root password for the database | [optional] 
**internal_port** | **int** | The internal port of the database | [optional] 
**id** | **str** | The unique ID of the database | [optional] 
**hourly_price** | **float** | The hourly price of the database | [optional] 
**meta_data** | [**DBDetailsDatabaseMetaData**](DBDetailsDatabaseMetaData.md) |  | [optional] 
**username** | **str** | The username associated with the database | [optional] 

## Example

```python
from openapi_client.models.db_details_database import DBDetailsDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of DBDetailsDatabase from a JSON string
db_details_database_instance = DBDetailsDatabase.from_json(json)
# print the JSON string representation of the object
print DBDetailsDatabase.to_json()

# convert the object into a dict
db_details_database_dict = db_details_database_instance.to_dict()
# create an instance of DBDetailsDatabase from a dict
db_details_database_form_dict = db_details_database.from_dict(db_details_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


