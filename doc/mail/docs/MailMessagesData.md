# MailMessagesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**messages** | [**List[MailMessage]**](MailMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_messages_data import MailMessagesData

# TODO update the JSON string below
json = "{}"
# create an instance of MailMessagesData from a JSON string
mail_messages_data_instance = MailMessagesData.from_json(json)
# print the JSON string representation of the object
print MailMessagesData.to_json()

# convert the object into a dict
mail_messages_data_dict = mail_messages_data_instance.to_dict()
# create an instance of MailMessagesData from a dict
mail_messages_data_form_dict = mail_messages_data.from_dict(mail_messages_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


