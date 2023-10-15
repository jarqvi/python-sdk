# SMTP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**SMTPData**](SMTPData.md) |  | [optional] 

## Example

```python
from openapi_client.models.smtp import SMTP

# TODO update the JSON string below
json = "{}"
# create an instance of SMTP from a JSON string
smtp_instance = SMTP.from_json(json)
# print the JSON string representation of the object
print SMTP.to_json()

# convert the object into a dict
smtp_dict = smtp_instance.to_dict()
# create an instance of SMTP from a dict
smtp_form_dict = smtp.from_dict(smtp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


