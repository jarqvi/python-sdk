# RemainingFreeMails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**RemainingFreeMailsData**](RemainingFreeMailsData.md) |  | [optional] 

## Example

```python
from openapi_client.models.remaining_free_mails import RemainingFreeMails

# TODO update the JSON string below
json = "{}"
# create an instance of RemainingFreeMails from a JSON string
remaining_free_mails_instance = RemainingFreeMails.from_json(json)
# print the JSON string representation of the object
print RemainingFreeMails.to_json()

# convert the object into a dict
remaining_free_mails_dict = remaining_free_mails_instance.to_dict()
# create an instance of RemainingFreeMails from a dict
remaining_free_mails_form_dict = remaining_free_mails.from_dict(remaining_free_mails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


