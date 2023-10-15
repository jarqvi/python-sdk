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

class CheckDNSResponseDnsSetupSpf(BaseModel):
    """
    CheckDNSResponseDnsSetupSpf
    """
    spf_error: Optional[StrictStr] = None
    spf_record: Optional[StrictStr] = None
    spf_status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["spf_error", "spf_record", "spf_status"]

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
    def from_json(cls, json_str: str) -> CheckDNSResponseDnsSetupSpf:
        """Create an instance of CheckDNSResponseDnsSetupSpf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckDNSResponseDnsSetupSpf:
        """Create an instance of CheckDNSResponseDnsSetupSpf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckDNSResponseDnsSetupSpf.model_validate(obj)

        _obj = CheckDNSResponseDnsSetupSpf.model_validate({
            "spf_error": obj.get("spf_error"),
            "spf_record": obj.get("spf_record"),
            "spf_status": obj.get("spf_status")
        })
        return _obj


