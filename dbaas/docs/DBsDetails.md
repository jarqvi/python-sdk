# DBsDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | [**List[DBsDetailsDatabasesInner]**](DBsDetailsDatabasesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.dbs_details import DBsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DBsDetails from a JSON string
dbs_details_instance = DBsDetails.from_json(json)
# print the JSON string representation of the object
print DBsDetails.to_json()

# convert the object into a dict
dbs_details_dict = dbs_details_instance.to_dict()
# create an instance of DBsDetails from a dict
dbs_details_form_dict = dbs_details.from_dict(dbs_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


