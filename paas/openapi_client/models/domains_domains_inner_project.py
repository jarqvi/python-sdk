# coding: utf-8

"""
    PaaS

    Manage your apps using our API  [wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>]( wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>)  Parameters: - `token`: Your api token in liara - `cmd`: By default /bin/bash - `project_id`: The id of your project in liara  This `WebSocket` endpoint allows `real-time` communication with the projects service hosted at `Liara` You can use `WebSocket protocols` to send and receive data, enabling efficient and low-latency interactions with the projects

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field

class DomainsDomainsInnerProject(BaseModel):
    """
    The type of domain  # noqa: E501
    """
    id: Optional[StrictStr] = Field(default=None, description="The id of project", alias="_id")
    project_id: Optional[StrictStr] = Field(default=None, description="The name of project")
    __properties: ClassVar[List[str]] = ["_id", "project_id"]

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
    def from_json(cls, json_str: str) -> DomainsDomainsInnerProject:
        """Create an instance of DomainsDomainsInnerProject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DomainsDomainsInnerProject:
        """Create an instance of DomainsDomainsInnerProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DomainsDomainsInnerProject.model_validate(obj)

        _obj = DomainsDomainsInnerProject.model_validate({
            "_id": obj.get("_id"),
            "project_id": obj.get("project_id")
        })
        return _obj


