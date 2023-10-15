# DomainsDomainsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of domain | [optional] 
**name** | **str** | The name of domain | [optional] 
**type** | **str** | The type of domain | [optional] 
**project** | [**DomainsDomainsInnerProject**](DomainsDomainsInnerProject.md) |  | [optional] 
**status** | **str** | The status of domain | [optional] 
**certificates_status** | **str** | The certificatesStatus of domain | [optional] 
**redirect_to** | **str** | The redirectTo of domain | [optional] 
**redirect_status** | **float** | The redirectStatus of domain | [optional] 
**created_at** | **str** | The created_at of domain | [optional] 
**c_name_record** | **str** | The CNameRecord of domain | [optional] 

## Example

```python
from openapi_client.models.domains_domains_inner import DomainsDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsDomainsInner from a JSON string
domains_domains_inner_instance = DomainsDomainsInner.from_json(json)
# print the JSON string representation of the object
print DomainsDomainsInner.to_json()

# convert the object into a dict
domains_domains_inner_dict = domains_domains_inner_instance.to_dict()
# create an instance of DomainsDomainsInner from a dict
domains_domains_inner_form_dict = domains_domains_inner.from_dict(domains_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


