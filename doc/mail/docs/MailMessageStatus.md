# MailMessageStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mail_message_status import MailMessageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MailMessageStatus from a JSON string
mail_message_status_instance = MailMessageStatus.from_json(json)
# print the JSON string representation of the object
print MailMessageStatus.to_json()

# convert the object into a dict
mail_message_status_dict = mail_message_status_instance.to_dict()
# create an instance of MailMessageStatus from a dict
mail_message_status_form_dict = mail_message_status.from_dict(mail_message_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


