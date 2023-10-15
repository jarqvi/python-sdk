# MailForwardsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarders** | [**List[MailForwardsDataForwardersInner]**](MailForwardsDataForwardersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_forwards_data import MailForwardsData

# TODO update the JSON string below
json = "{}"
# create an instance of MailForwardsData from a JSON string
mail_forwards_data_instance = MailForwardsData.from_json(json)
# print the JSON string representation of the object
print MailForwardsData.to_json()

# convert the object into a dict
mail_forwards_data_dict = mail_forwards_data_instance.to_dict()
# create an instance of MailForwardsData from a dict
mail_forwards_data_form_dict = mail_forwards_data.from_dict(mail_forwards_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


