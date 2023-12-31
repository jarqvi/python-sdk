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

class CheckDNSResponseDnsSetupReturnPath(BaseModel):
    """
    CheckDNSResponseDnsSetupReturnPath
    """
    return_path_domain: Optional[StrictStr] = None
    return_path_error: Optional[StrictStr] = None
    return_path_status: Optional[StrictStr] = None
    return_path_value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["return_path_domain", "return_path_error", "return_path_status", "return_path_value"]

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
    def from_json(cls, json_str: str) -> CheckDNSResponseDnsSetupReturnPath:
        """Create an instance of CheckDNSResponseDnsSetupReturnPath from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckDNSResponseDnsSetupReturnPath:
        """Create an instance of CheckDNSResponseDnsSetupReturnPath from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckDNSResponseDnsSetupReturnPath.model_validate(obj)

        _obj = CheckDNSResponseDnsSetupReturnPath.model_validate({
            "return_path_domain": obj.get("return_path_domain"),
            "return_path_error": obj.get("return_path_error"),
            "return_path_status": obj.get("return_path_status"),
            "return_path_value": obj.get("return_path_value")
        })
        return _obj


