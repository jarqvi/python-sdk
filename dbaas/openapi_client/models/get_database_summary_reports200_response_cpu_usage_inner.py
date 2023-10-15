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


from typing import List, Optional
from pydantic import BaseModel, StrictStr
from openapi_client.models.get_database_summary_reports200_response_cpu_usage_inner_value_inner import GetDatabaseSummaryReports200ResponseCpuUsageInnerValueInner

class GetDatabaseSummaryReports200ResponseCpuUsageInner(BaseModel):
    """
    GetDatabaseSummaryReports200ResponseCpuUsageInner
    """
    value: Optional[List[GetDatabaseSummaryReports200ResponseCpuUsageInnerValueInner]] = None
    applet: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["value", "applet"]

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
    def from_json(cls, json_str: str) -> GetDatabaseSummaryReports200ResponseCpuUsageInner:
        """Create an instance of GetDatabaseSummaryReports200ResponseCpuUsageInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in value (list)
        _items = []
        if self.value:
            for _item in self.value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['value'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetDatabaseSummaryReports200ResponseCpuUsageInner:
        """Create an instance of GetDatabaseSummaryReports200ResponseCpuUsageInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetDatabaseSummaryReports200ResponseCpuUsageInner.model_validate(obj)

        _obj = GetDatabaseSummaryReports200ResponseCpuUsageInner.model_validate({
            "value": [GetDatabaseSummaryReports200ResponseCpuUsageInnerValueInner.from_dict(_item) for _item in obj.get("value")] if obj.get("value") is not None else None,
            "applet": obj.get("applet")
        })
        return _obj


