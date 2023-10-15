# MailAttachments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailAttachmentsData**](MailAttachmentsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_attachments import MailAttachments

# TODO update the JSON string below
json = "{}"
# create an instance of MailAttachments from a JSON string
mail_attachments_instance = MailAttachments.from_json(json)
# print the JSON string representation of the object
print MailAttachments.to_json()

# convert the object into a dict
mail_attachments_dict = mail_attachments_instance.to_dict()
# create an instance of MailAttachments from a dict
mail_attachments_form_dict = mail_attachments.from_dict(mail_attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


