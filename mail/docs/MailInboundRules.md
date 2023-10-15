# MailInboundRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailInboundRulesData**](MailInboundRulesData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_inbound_rules import MailInboundRules

# TODO update the JSON string below
json = "{}"
# create an instance of MailInboundRules from a JSON string
mail_inbound_rules_instance = MailInboundRules.from_json(json)
# print the JSON string representation of the object
print MailInboundRules.to_json()

# convert the object into a dict
mail_inbound_rules_dict = mail_inbound_rules_instance.to_dict()
# create an instance of MailInboundRules from a dict
mail_inbound_rules_form_dict = mail_inbound_rules.from_dict(mail_inbound_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


