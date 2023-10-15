# RedirectDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_status** | **float** | 302 or 301 | 
**redirect_to** | **str** |  | 

## Example

```python
from openapi_client.models.redirect_domain_request import RedirectDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectDomainRequest from a JSON string
redirect_domain_request_instance = RedirectDomainRequest.from_json(json)
# print the JSON string representation of the object
print RedirectDomainRequest.to_json()

# convert the object into a dict
redirect_domain_request_dict = redirect_domain_request_instance.to_dict()
# create an instance of RedirectDomainRequest from a dict
redirect_domain_request_form_dict = redirect_domain_request.from_dict(redirect_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


