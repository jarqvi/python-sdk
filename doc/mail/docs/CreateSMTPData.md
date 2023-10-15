# CreateSMTPData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**passowrd** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_smtp_data import CreateSMTPData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSMTPData from a JSON string
create_smtp_data_instance = CreateSMTPData.from_json(json)
# print the JSON string representation of the object
print CreateSMTPData.to_json()

# convert the object into a dict
create_smtp_data_dict = create_smtp_data_instance.to_dict()
# create an instance of CreateSMTPData from a dict
create_smtp_data_form_dict = create_smtp_data.from_dict(create_smtp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


