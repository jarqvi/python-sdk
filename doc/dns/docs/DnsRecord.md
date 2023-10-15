# DnsRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of dns record, \&quot;@\&quot; for zone name(root level), \&quot;*\&quot; for wild card and any valid value with RFC 1123 | [optional] 
**type** | **str** | The type of dns record, valid values: [A, AAAA, TXT, CNAME, ALIAS, MX, SRV, SPF, PTR] | [optional] 
**ttl** | **float** | The ttl of dns record, is not required, valid values: [120, 180, 300, 600, 900, 1800, 3600, 7200, 18000, 43200, 86400, 172800, 432000] | [optional] 
**contents** | **List[object]** | Array of content of dns record, change base on type of dns record | [optional] 

## Example

```python
from openapi_client.models.dns_record import DnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecord from a JSON string
dns_record_instance = DnsRecord.from_json(json)
# print the JSON string representation of the object
print DnsRecord.to_json()

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DnsRecord from a dict
dns_record_form_dict = dns_record.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


