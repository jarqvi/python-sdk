# DnsRecordId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of dns record which need in PUT, DELETE and GET method | [optional] 
**name** | **str** | The name of dns record, \&quot;@\&quot; for zone name(root level), \&quot;*\&quot; for wild card and any valid value with RFC 1123 | [optional] 
**type** | **str** | The type of dns record, valid values: [A, AAAA, TXT, CNAME, ALIAS, MX, SRV, CAA] | [optional] 
**ttl** | **float** | The ttl of dns record, is not required, valid values: [120, 180, 300, 600, 900, 1800, 3600, 7200, 18000, 43200, 86400, 172800, 432000] | [optional] 
**contents** | **List[object]** | Array of content of dns record, change base on type of dns record | [optional] 

## Example

```python
from openapi_client.models.dns_record_id import DnsRecordId

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordId from a JSON string
dns_record_id_instance = DnsRecordId.from_json(json)
# print the JSON string representation of the object
print DnsRecordId.to_json()

# convert the object into a dict
dns_record_id_dict = dns_record_id_instance.to_dict()
# create an instance of DnsRecordId from a dict
dns_record_id_form_dict = dns_record_id.from_dict(dns_record_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


