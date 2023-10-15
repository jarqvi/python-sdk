# coding: utf-8

"""
    Liara Mail API Documentaion

    A fully featured mail delivery platform for incoming & outgoing e-mail

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from openapi_client.models.check_dns_data import CheckDNSData

class CheckDNS(BaseModel):
    """
    CheckDNS
    """
    status: Optional[StrictStr] = None
    data: Optional[CheckDNSData] = None
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
    def from_json(cls, json_str: str) -> CheckDNS:
        """Create an instance of CheckDNS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckDNS:
        """Create an instance of CheckDNS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckDNS.model_validate(obj)

        _obj = CheckDNS.model_validate({
            "status": obj.get("status"),
            "data": CheckDNSData.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj


