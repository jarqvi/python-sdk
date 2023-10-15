# DBDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**DBDetailsDatabase**](DBDetailsDatabase.md) |  | [optional] 

## Example

```python
from openapi_client.models.db_details import DBDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DBDetails from a JSON string
db_details_instance = DBDetails.from_json(json)
# print the JSON string representation of the object
print DBDetails.to_json()

# convert the object into a dict
db_details_dict = db_details_instance.to_dict()
# create an instance of DBDetails from a dict
db_details_form_dict = db_details.from_dict(db_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


