# DnsRecordResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | success | [optional] 
**data** | [**DnsRecordId**](DnsRecordId.md) |  | [optional] 

## Example

```python
from openapi_client.models.dns_record_response import DnsRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordResponse from a JSON string
dns_record_response_instance = DnsRecordResponse.from_json(json)
# print the JSON string representation of the object
print DnsRecordResponse.to_json()

# convert the object into a dict
dns_record_response_dict = dns_record_response_instance.to_dict()
# create an instance of DnsRecordResponse from a dict
dns_record_response_form_dict = dns_record_response.from_dict(dns_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


