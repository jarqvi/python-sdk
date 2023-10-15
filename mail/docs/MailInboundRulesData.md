# MailInboundRulesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_inboundrules** | [**List[MailInboundRulesDataMailInboundrulesInner]**](MailInboundRulesDataMailInboundrulesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_inbound_rules_data import MailInboundRulesData

# TODO update the JSON string below
json = "{}"
# create an instance of MailInboundRulesData from a JSON string
mail_inbound_rules_data_instance = MailInboundRulesData.from_json(json)
# print the JSON string representation of the object
print MailInboundRulesData.to_json()

# convert the object into a dict
mail_inbound_rules_data_dict = mail_inbound_rules_data_instance.to_dict()
# create an instance of MailInboundRulesData from a dict
mail_inbound_rules_data_form_dict = mail_inbound_rules_data.from_dict(mail_inbound_rules_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


