# CountMailPerDay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**CountMailPerDayData**](CountMailPerDayData.md) |  | [optional] 

## Example

```python
from openapi_client.models.count_mail_per_day import CountMailPerDay

# TODO update the JSON string below
json = "{}"
# create an instance of CountMailPerDay from a JSON string
count_mail_per_day_instance = CountMailPerDay.from_json(json)
# print the JSON string representation of the object
print CountMailPerDay.to_json()

# convert the object into a dict
count_mail_per_day_dict = count_mail_per_day_instance.to_dict()
# create an instance of CountMailPerDay from a dict
count_mail_per_day_form_dict = count_mail_per_day.from_dict(count_mail_per_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


