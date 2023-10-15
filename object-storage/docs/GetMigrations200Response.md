# GetMigrations200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**migrations** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.get_migrations200_response import GetMigrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMigrations200Response from a JSON string
get_migrations200_response_instance = GetMigrations200Response.from_json(json)
# print the JSON string representation of the object
print GetMigrations200Response.to_json()

# convert the object into a dict
get_migrations200_response_dict = get_migrations200_response_instance.to_dict()
# create an instance of GetMigrations200Response from a dict
get_migrations200_response_form_dict = get_migrations200_response.from_dict(get_migrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


