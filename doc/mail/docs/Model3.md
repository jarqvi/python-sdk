# Model3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**subject** | **str** |  | 
**to** | **str** |  | 
**var_from** | **str** |  | 
**reply_to** | **str** |  | [optional] 
**attachments** | [**List[Model2]**](Model2.md) |  | [optional] 

## Example

```python
from openapi_client.models.model3 import Model3

# TODO update the JSON string below
json = "{}"
# create an instance of Model3 from a JSON string
model3_instance = Model3.from_json(json)
# print the JSON string representation of the object
print Model3.to_json()

# convert the object into a dict
model3_dict = model3_instance.to_dict()
# create an instance of Model3 from a dict
model3_form_dict = model3.from_dict(model3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


