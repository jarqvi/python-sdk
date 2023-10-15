# CountMailPerDayData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_per_day** | [**List[CountMailPerDayDataEmailPerDayInner]**](CountMailPerDayDataEmailPerDayInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.count_mail_per_day_data import CountMailPerDayData

# TODO update the JSON string below
json = "{}"
# create an instance of CountMailPerDayData from a JSON string
count_mail_per_day_data_instance = CountMailPerDayData.from_json(json)
# print the JSON string representation of the object
print CountMailPerDayData.to_json()

# convert the object into a dict
count_mail_per_day_data_dict = count_mail_per_day_data_instance.to_dict()
# create an instance of CountMailPerDayData from a dict
count_mail_per_day_data_form_dict = count_mail_per_day_data.from_dict(count_mail_per_day_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


