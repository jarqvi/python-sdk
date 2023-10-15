# CheckDNSResponseDnsSetupDkim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dkim_error** | **str** |  | [optional] 
**dkim_record** | **str** |  | [optional] 
**dkim_record_name** | **str** |  | [optional] 
**dkim_status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_response_dns_setup_dkim import CheckDNSResponseDnsSetupDkim

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSResponseDnsSetupDkim from a JSON string
check_dns_response_dns_setup_dkim_instance = CheckDNSResponseDnsSetupDkim.from_json(json)
# print the JSON string representation of the object
print CheckDNSResponseDnsSetupDkim.to_json()

# convert the object into a dict
check_dns_response_dns_setup_dkim_dict = check_dns_response_dns_setup_dkim_instance.to_dict()
# create an instance of CheckDNSResponseDnsSetupDkim from a dict
check_dns_response_dns_setup_dkim_form_dict = check_dns_response_dns_setup_dkim.from_dict(check_dns_response_dns_setup_dkim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


