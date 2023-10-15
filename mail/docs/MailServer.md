# MailServer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailServerData**](MailServerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_server import MailServer

# TODO update the JSON string below
json = "{}"
# create an instance of MailServer from a JSON string
mail_server_instance = MailServer.from_json(json)
# print the JSON string representation of the object
print MailServer.to_json()

# convert the object into a dict
mail_server_dict = mail_server_instance.to_dict()
# create an instance of MailServer from a dict
mail_server_form_dict = mail_server.from_dict(mail_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


