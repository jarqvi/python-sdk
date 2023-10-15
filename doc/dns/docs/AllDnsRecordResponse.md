# AllDnsRecordResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | success | [optional] 
**data** | [**List[DnsRecordId]**](DnsRecordId.md) |  | [optional] 

## Example

```python
from openapi_client.models.all_dns_record_response import AllDnsRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllDnsRecordResponse from a JSON string
all_dns_record_response_instance = AllDnsRecordResponse.from_json(json)
# print the JSON string representation of the object
print AllDnsRecordResponse.to_json()

# convert the object into a dict
all_dns_record_response_dict = all_dns_record_response_instance.to_dict()
# create an instance of AllDnsRecordResponse from a dict
all_dns_record_response_form_dict = all_dns_record_response.from_dict(all_dns_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


