# CheckDNSResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_setup** | [**CheckDNSResponseDnsSetup**](CheckDNSResponseDnsSetup.md) |  | [optional] 
**user** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**records_status** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**check_dns_record** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**smtp_server** | **str** |  | [optional] 
**smtp_port** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.check_dns_response import CheckDNSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDNSResponse from a JSON string
check_dns_response_instance = CheckDNSResponse.from_json(json)
# print the JSON string representation of the object
print CheckDNSResponse.to_json()

# convert the object into a dict
check_dns_response_dict = check_dns_response_instance.to_dict()
# create an instance of CheckDNSResponse from a dict
check_dns_response_form_dict = check_dns_response.from_dict(check_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


