# MailForwards


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailForwardsData**](MailForwardsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_forwards import MailForwards

# TODO update the JSON string below
json = "{}"
# create an instance of MailForwards from a JSON string
mail_forwards_instance = MailForwards.from_json(json)
# print the JSON string representation of the object
print MailForwards.to_json()

# convert the object into a dict
mail_forwards_dict = mail_forwards_instance.to_dict()
# create an instance of MailForwards from a dict
mail_forwards_form_dict = mail_forwards.from_dict(mail_forwards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


