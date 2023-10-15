# SMTPDataCredentialsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.smtp_data_credentials_inner import SMTPDataCredentialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SMTPDataCredentialsInner from a JSON string
smtp_data_credentials_inner_instance = SMTPDataCredentialsInner.from_json(json)
# print the JSON string representation of the object
print SMTPDataCredentialsInner.to_json()

# convert the object into a dict
smtp_data_credentials_inner_dict = smtp_data_credentials_inner_instance.to_dict()
# create an instance of SMTPDataCredentialsInner from a dict
smtp_data_credentials_inner_form_dict = smtp_data_credentials_inner.from_dict(smtp_data_credentials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


