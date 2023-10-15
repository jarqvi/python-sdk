# CheckDNSResponseDnsSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim** | [**CheckDNSResponseDnsSetupDkim**](CheckDNSResponseDnsSetupDkim.md) |  | [optional] 
**mx_record** | [**CheckDNSResponseDnsSetupMxRecord**](CheckDNSResponseDnsSetupMxRecord.md) |  | [optional] 
**return_path** | [**CheckDNSResponseDnsSetupReturnPath**](CheckDNSResponseDnsSetupReturnPath.md) |  | [optional] 
**spf** | [**CheckDNSResponseDnsSetupSpf**](CheckDNSResponseDnsSetupSpf.md) |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_response_dns_setup import CheckDNSResponseDnsSetup

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSResponseDnsSetup from a JSON string
check_dns_response_dns_setup_instance = CheckDNSResponseDnsSetup.from_json(json)
# print the JSON string representation of the object
print CheckDNSResponseDnsSetup.to_json()

# convert the object into a dict
check_dns_response_dns_setup_dict = check_dns_response_dns_setup_instance.to_dict()
# create an instance of CheckDNSResponseDnsSetup from a dict
check_dns_response_dns_setup_form_dict = check_dns_response_dns_setup.from_dict(check_dns_response_dns_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


