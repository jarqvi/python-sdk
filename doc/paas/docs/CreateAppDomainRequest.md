# CreateAppDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project** | **str** |  | 
**type** | **str** |  | [default to 'PROJECT']

## Example

```python
from openapi_client.models.create_app_domain_request import CreateAppDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppDomainRequest from a JSON string
create_app_domain_request_instance = CreateAppDomainRequest.from_json(json)
# print the JSON string representation of the object
print CreateAppDomainRequest.to_json()

# convert the object into a dict
create_app_domain_request_dict = create_app_domain_request_instance.to_dict()
# create an instance of CreateAppDomainRequest from a dict
create_app_domain_request_form_dict = create_app_domain_request.from_dict(create_app_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


