# MailMessages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailMessagesData**](MailMessagesData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_messages import MailMessages

# TODO update the JSON string below
json = "{}"
# create an instance of MailMessages from a JSON string
mail_messages_instance = MailMessages.from_json(json)
# print the JSON string representation of the object
print MailMessages.to_json()

# convert the object into a dict
mail_messages_dict = mail_messages_instance.to_dict()
# create an instance of MailMessages from a dict
mail_messages_form_dict = mail_messages.from_dict(mail_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


