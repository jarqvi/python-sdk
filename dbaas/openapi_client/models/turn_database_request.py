# coding: utf-8

"""
    DBaaS

    Manage your databases using our API

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, StrictFloat, StrictInt

class TurnDatabaseRequest(BaseModel):
    """
    TurnDatabaseRequest
    """
    scale: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["scale"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TurnDatabaseRequest:
        """Create an instance of TurnDatabaseRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TurnDatabaseRequest:
        """Create an instance of TurnDatabaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TurnDatabaseRequest.model_validate(obj)

        _obj = TurnDatabaseRequest.model_validate({
            "scale": obj.get("scale")
        })
        return _obj


