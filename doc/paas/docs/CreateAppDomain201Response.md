# CreateAppDomain201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**CreateAppDomain201ResponseDomain**](CreateAppDomain201ResponseDomain.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_app_domain201_response import CreateAppDomain201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppDomain201Response from a JSON string
create_app_domain201_response_instance = CreateAppDomain201Response.from_json(json)
# print the JSON string representation of the object
print CreateAppDomain201Response.to_json()

# convert the object into a dict
create_app_domain201_response_dict = create_app_domain201_response_instance.to_dict()
# create an instance of CreateAppDomain201Response from a dict
create_app_domain201_response_form_dict = create_app_domain201_response.from_dict(create_app_domain201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


