# MailServerResponseRateLimitTier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** |  | [optional] 
**daily** | **float** |  | [optional] 
**monthly** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.mail_server_response_rate_limit_tier import MailServerResponseRateLimitTier

# TODO update the JSON string below
json = "{}"
# create an instance of MailServerResponseRateLimitTier from a JSON string
mail_server_response_rate_limit_tier_instance = MailServerResponseRateLimitTier.from_json(json)
# print the JSON string representation of the object
print MailServerResponseRateLimitTier.to_json()

# convert the object into a dict
mail_server_response_rate_limit_tier_dict = mail_server_response_rate_limit_tier_instance.to_dict()
# create an instance of MailServerResponseRateLimitTier from a dict
mail_server_response_rate_limit_tier_form_dict = mail_server_response_rate_limit_tier.from_dict(mail_server_response_rate_limit_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


