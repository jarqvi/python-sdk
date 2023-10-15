# MailAccounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailAccountsData**](MailAccountsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_accounts import MailAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of MailAccounts from a JSON string
mail_accounts_instance = MailAccounts.from_json(json)
# print the JSON string representation of the object
print MailAccounts.to_json()

# convert the object into a dict
mail_accounts_dict = mail_accounts_instance.to_dict()
# create an instance of MailAccounts from a dict
mail_accounts_form_dict = mail_accounts.from_dict(mail_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


