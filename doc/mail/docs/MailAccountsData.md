# MailAccountsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**accounts** | [**List[MailAccountsDataAccountsInner]**](MailAccountsDataAccountsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_accounts_data import MailAccountsData

# TODO update the JSON string below
json = "{}"
# create an instance of MailAccountsData from a JSON string
mail_accounts_data_instance = MailAccountsData.from_json(json)
# print the JSON string representation of the object
print MailAccountsData.to_json()

# convert the object into a dict
mail_accounts_data_dict = mail_accounts_data_instance.to_dict()
# create an instance of MailAccountsData from a dict
mail_accounts_data_form_dict = mail_accounts_data.from_dict(mail_accounts_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


