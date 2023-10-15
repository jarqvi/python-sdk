# coding: utf-8

"""
    DNS

    Manage dns zones and records

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr
from openapi_client.models.zone import Zone

class Zones(BaseModel):
    """
    Zones
    """
    status: Optional[StrictStr] = None
    data: Optional[List[Zone]] = None
    __properties: ClassVar[List[str]] = ["status", "data"]

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
    def from_json(cls, json_str: str) -> Zones:
        """Create an instance of Zones from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Zones:
        """Create an instance of Zones from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Zones.model_validate(obj)

        _obj = Zones.model_validate({
            "status": obj.get("status"),
            "data": [Zone.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj


