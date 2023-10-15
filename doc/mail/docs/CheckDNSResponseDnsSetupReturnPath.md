# CheckDNSResponseDnsSetupReturnPath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_path_domain** | **str** |  | [optional] 
**return_path_error** | **str** |  | [optional] 
**return_path_status** | **str** |  | [optional] 
**return_path_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_response_dns_setup_return_path import CheckDNSResponseDnsSetupReturnPath

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSResponseDnsSetupReturnPath from a JSON string
check_dns_response_dns_setup_return_path_instance = CheckDNSResponseDnsSetupReturnPath.from_json(json)
# print the JSON string representation of the object
print CheckDNSResponseDnsSetupReturnPath.to_json()

# convert the object into a dict
check_dns_response_dns_setup_return_path_dict = check_dns_response_dns_setup_return_path_instance.to_dict()
# create an instance of CheckDNSResponseDnsSetupReturnPath from a dict
check_dns_response_dns_setup_return_path_form_dict = check_dns_response_dns_setup_return_path.from_dict(check_dns_response_dns_setup_return_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


