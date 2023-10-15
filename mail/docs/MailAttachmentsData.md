# MailAttachmentsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[MailAttachment]**](MailAttachment.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_attachments_data import MailAttachmentsData

# TODO update the JSON string below
json = "{}"
# create an instance of MailAttachmentsData from a JSON string
mail_attachments_data_instance = MailAttachmentsData.from_json(json)
# print the JSON string representation of the object
print MailAttachmentsData.to_json()

# convert the object into a dict
mail_attachments_data_dict = mail_attachments_data_instance.to_dict()
# create an instance of MailAttachmentsData from a dict
mail_attachments_data_form_dict = mail_attachments_data.from_dict(mail_attachments_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


