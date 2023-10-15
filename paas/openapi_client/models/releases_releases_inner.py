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


from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.releases_releases_inner_git_info import ReleasesReleasesInnerGitInfo

class ReleasesReleasesInner(BaseModel):
    """
    ReleasesReleasesInner
    """
    id: Optional[StrictStr] = Field(default=None, description="The id of release", alias="_id")
    type: Optional[StrictStr] = Field(default=None, description="The type of release")
    image_name: Optional[StrictStr] = Field(default=None, description="The imageName of release", alias="imageName")
    project_type: Optional[StrictStr] = Field(default=None, description="The projectType of release", alias="projectType")
    state: Optional[StrictStr] = Field(default=None, description="The state of release")
    port: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The port of release")
    git_info: Optional[ReleasesReleasesInnerGitInfo] = Field(default=None, alias="gitInfo")
    client: Optional[StrictStr] = Field(default=None, description="The client of release")
    finished_at: Optional[StrictStr] = Field(default=None, description="The finishedAt of release", alias="finishedAt")
    created_at: Optional[StrictStr] = Field(default=None, description="The createdAt of release", alias="createdAt")
    tag: Optional[StrictStr] = Field(default=None, description="The tag of release")
    source_available: Optional[StrictBool] = Field(default=None, description="The sourceAvailable of release", alias="sourceAvailable")
    __properties: ClassVar[List[str]] = ["_id", "type", "imageName", "projectType", "state", "port", "gitInfo", "client", "finishedAt", "createdAt", "tag", "sourceAvailable"]

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
    def from_json(cls, json_str: str) -> ReleasesReleasesInner:
        """Create an instance of ReleasesReleasesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of git_info
        if self.git_info:
            _dict['gitInfo'] = self.git_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReleasesReleasesInner:
        """Create an instance of ReleasesReleasesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReleasesReleasesInner.model_validate(obj)

        _obj = ReleasesReleasesInner.model_validate({
            "_id": obj.get("_id"),
            "type": obj.get("type"),
            "imageName": obj.get("imageName"),
            "projectType": obj.get("projectType"),
            "state": obj.get("state"),
            "port": obj.get("port"),
            "gitInfo": ReleasesReleasesInnerGitInfo.from_dict(obj.get("gitInfo")) if obj.get("gitInfo") is not None else None,
            "client": obj.get("client"),
            "finishedAt": obj.get("finishedAt"),
            "createdAt": obj.get("createdAt"),
            "tag": obj.get("tag"),
            "sourceAvailable": obj.get("sourceAvailable")
        })
        return _obj


