# DBsDetailsDatabasesInner


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
**created_at** | **str** | The creation timestamp of the database | [optional] 
**internal_port** | **int** | The internal port of the database | [optional] 
**id** | **str** | The unique ID of the database | [optional] 

## Example

```python
from openapi_client.models.dbs_details_databases_inner import DBsDetailsDatabasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DBsDetailsDatabasesInner from a JSON string
dbs_details_databases_inner_instance = DBsDetailsDatabasesInner.from_json(json)
# print the JSON string representation of the object
print DBsDetailsDatabasesInner.to_json()

# convert the object into a dict
dbs_details_databases_inner_dict = dbs_details_databases_inner_instance.to_dict()
# create an instance of DBsDetailsDatabasesInner from a dict
dbs_details_databases_inner_form_dict = dbs_details_databases_inner.from_dict(dbs_details_databases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


