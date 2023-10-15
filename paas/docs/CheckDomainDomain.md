# CheckDomainDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**project** | [**CheckDomainDomainProject**](CheckDomainDomainProject.md) |  | [optional] 
**status** | **str** |  | [optional] 
**certificates_status** | **str** |  | [optional] 
**redirect_to** | **str** |  | [optional] 
**redirect_status** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**punycode_name** | **str** |  | [optional] 
**verification_code** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**v** | **float** |  | [optional] 
**c_name_record** | **str** |  | [optional] 
**issued_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.check_domain_domain import CheckDomainDomain

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDomainDomain from a JSON string
check_domain_domain_instance = CheckDomainDomain.from_json(json)
# print the JSON string representation of the object
print CheckDomainDomain.to_json()

# convert the object into a dict
check_domain_domain_dict = check_domain_domain_instance.to_dict()
# create an instance of CheckDomainDomain from a dict
check_domain_domain_form_dict = check_domain_domain.from_dict(check_domain_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


