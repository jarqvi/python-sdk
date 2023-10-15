# MailServersData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_servers** | [**List[MailServerResponse]**](MailServerResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_servers_data import MailServersData

# TODO update the JSON string below
json = "{}"
# create an instance of MailServersData from a JSON string
mail_servers_data_instance = MailServersData.from_json(json)
# print the JSON string representation of the object
print MailServersData.to_json()

# convert the object into a dict
mail_servers_data_dict = mail_servers_data_instance.to_dict()
# create an instance of MailServersData from a dict
mail_servers_data_form_dict = mail_servers_data.from_dict(mail_servers_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


