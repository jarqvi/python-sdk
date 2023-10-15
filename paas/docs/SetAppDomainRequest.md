# SetAppDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**project_id** | **str** |  | 

## Example

```python
from openapi_client.models.set_app_domain_request import SetAppDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppDomainRequest from a JSON string
set_app_domain_request_instance = SetAppDomainRequest.from_json(json)
# print the JSON string representation of the object
print SetAppDomainRequest.to_json()

# convert the object into a dict
set_app_domain_request_dict = set_app_domain_request_instance.to_dict()
# create an instance of SetAppDomainRequest from a dict
set_app_domain_request_form_dict = set_app_domain_request.from_dict(set_app_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


