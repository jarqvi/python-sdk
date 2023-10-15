# MailMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**has_html** | **bool** |  | [optional] 
**is_dev** | **bool** |  | [optional] 
**is_free** | **bool** |  | [optional] 
**spam_score** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**status** | [**MailMessageStatus**](MailMessageStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**spam_reson** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.mail_message import MailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MailMessage from a JSON string
mail_message_instance = MailMessage.from_json(json)
# print the JSON string representation of the object
print MailMessage.to_json()

# convert the object into a dict
mail_message_dict = mail_message_instance.to_dict()
# create an instance of MailMessage from a dict
mail_message_form_dict = mail_message.from_dict(mail_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


