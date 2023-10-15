# MailServers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailServersData**](MailServersData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_servers import MailServers

# TODO update the JSON string below
json = "{}"
# create an instance of MailServers from a JSON string
mail_servers_instance = MailServers.from_json(json)
# print the JSON string representation of the object
print MailServers.to_json()

# convert the object into a dict
mail_servers_dict = mail_servers_instance.to_dict()
# create an instance of MailServers from a dict
mail_servers_form_dict = mail_servers.from_dict(mail_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


