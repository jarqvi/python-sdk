# CheckDNSResponseDnsSetupMxRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mx_error** | **str** |  | [optional] 
**mx_status** | **str** |  | [optional] 
**mx_record_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_response_dns_setup_mx_record import CheckDNSResponseDnsSetupMxRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSResponseDnsSetupMxRecord from a JSON string
check_dns_response_dns_setup_mx_record_instance = CheckDNSResponseDnsSetupMxRecord.from_json(json)
# print the JSON string representation of the object
print CheckDNSResponseDnsSetupMxRecord.to_json()

# convert the object into a dict
check_dns_response_dns_setup_mx_record_dict = check_dns_response_dns_setup_mx_record_instance.to_dict()
# create an instance of CheckDNSResponseDnsSetupMxRecord from a dict
check_dns_response_dns_setup_mx_record_form_dict = check_dns_response_dns_setup_mx_record.from_dict(check_dns_response_dns_setup_mx_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


