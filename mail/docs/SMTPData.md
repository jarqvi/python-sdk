# SMTPData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[SMTPDataCredentialsInner]**](SMTPDataCredentialsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.smtp_data import SMTPData

# TODO update the JSON string below
json = "{}"
# create an instance of SMTPData from a JSON string
smtp_data_instance = SMTPData.from_json(json)
# print the JSON string representation of the object
print SMTPData.to_json()

# convert the object into a dict
smtp_data_dict = smtp_data_instance.to_dict()
# create an instance of SMTPData from a dict
smtp_data_form_dict = smtp_data.from_dict(smtp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


