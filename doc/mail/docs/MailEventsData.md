# MailEventsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**events** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.mail_events_data import MailEventsData

# TODO update the JSON string below
json = "{}"
# create an instance of MailEventsData from a JSON string
mail_events_data_instance = MailEventsData.from_json(json)
# print the JSON string representation of the object
print MailEventsData.to_json()

# convert the object into a dict
mail_events_data_dict = mail_events_data_instance.to_dict()
# create an instance of MailEventsData from a dict
mail_events_data_form_dict = mail_events_data.from_dict(mail_events_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


