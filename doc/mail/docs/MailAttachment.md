# MailAttachment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **float** |  | [optional] 
**content_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mail_attachment import MailAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MailAttachment from a JSON string
mail_attachment_instance = MailAttachment.from_json(json)
# print the JSON string representation of the object
print MailAttachment.to_json()

# convert the object into a dict
mail_attachment_dict = mail_attachment_instance.to_dict()
# create an instance of MailAttachment from a dict
mail_attachment_form_dict = mail_attachment.from_dict(mail_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


