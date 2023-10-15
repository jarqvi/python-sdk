# MailEvents


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**MailEventsData**](MailEventsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_events import MailEvents

# TODO update the JSON string below
json = "{}"
# create an instance of MailEvents from a JSON string
mail_events_instance = MailEvents.from_json(json)
# print the JSON string representation of the object
print MailEvents.to_json()

# convert the object into a dict
mail_events_dict = mail_events_instance.to_dict()
# create an instance of MailEvents from a dict
mail_events_form_dict = mail_events.from_dict(mail_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


