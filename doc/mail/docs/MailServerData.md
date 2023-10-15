# MailServerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_server** | [**MailServerResponse**](MailServerResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_server_data import MailServerData

# TODO update the JSON string below
json = "{}"
# create an instance of MailServerData from a JSON string
mail_server_data_instance = MailServerData.from_json(json)
# print the JSON string representation of the object
print MailServerData.to_json()

# convert the object into a dict
mail_server_data_dict = mail_server_data_instance.to_dict()
# create an instance of MailServerData from a dict
mail_server_data_form_dict = mail_server_data.from_dict(mail_server_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


