# CheckDNS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**CheckDNSData**](CheckDNSData.md) |  | [optional] 

## Example

```python
from openapi_client.models.check_dns import CheckDNS

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNS from a JSON string
check_dns_instance = CheckDNS.from_json(json)
# print the JSON string representation of the object
print CheckDNS.to_json()

# convert the object into a dict
check_dns_dict = check_dns_instance.to_dict()
# create an instance of CheckDNS from a dict
check_dns_form_dict = check_dns.from_dict(check_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


