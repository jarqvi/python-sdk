# DBDetailsDatabaseNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the database node | [optional] 
**host** | **str** | The host of the database node | [optional] 

## Example

```python
from openapi_client.models.db_details_database_node import DBDetailsDatabaseNode

# TODO update the JSON string below
json = "{}"
# create an instance of DBDetailsDatabaseNode from a JSON string
db_details_database_node_instance = DBDetailsDatabaseNode.from_json(json)
# print the JSON string representation of the object
print DBDetailsDatabaseNode.to_json()

# convert the object into a dict
db_details_database_node_dict = db_details_database_node_instance.to_dict()
# create an instance of DBDetailsDatabaseNode from a dict
db_details_database_node_form_dict = db_details_database_node.from_dict(db_details_database_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


