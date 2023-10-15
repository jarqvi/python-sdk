# CheckDNSData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_server** | [**CheckDNSResponse**](CheckDNSResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_data import CheckDNSData

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSData from a JSON string
check_dns_data_instance = CheckDNSData.from_json(json)
# print the JSON string representation of the object
print CheckDNSData.to_json()

# convert the object into a dict
check_dns_data_dict = check_dns_data_instance.to_dict()
# create an instance of CheckDNSData from a dict
check_dns_data_form_dict = check_dns_data.from_dict(check_dns_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


