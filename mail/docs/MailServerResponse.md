# MailServerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_setup** | [**CheckDNSResponseDnsSetup**](CheckDNSResponseDnsSetup.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**records_status** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**rate_limit_tier** | [**MailServerResponseRateLimitTier**](MailServerResponseRateLimitTier.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**smtp_server** | **str** |  | [optional] 
**smtp_port** | **float** |  | [optional] 
**root_part_of_domain** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mail_server_response import MailServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MailServerResponse from a JSON string
mail_server_response_instance = MailServerResponse.from_json(json)
# print the JSON string representation of the object
print MailServerResponse.to_json()

# convert the object into a dict
mail_server_response_dict = mail_server_response_instance.to_dict()
# create an instance of MailServerResponse from a dict
mail_server_response_form_dict = mail_server_response.from_dict(mail_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


