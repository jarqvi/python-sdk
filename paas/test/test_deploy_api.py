# coding: utf-8

"""
    PaaS

    Manage your apps using our API  [wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>]( wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>)  Parameters: - `token`: Your api token in liara - `cmd`: By default /bin/bash - `project_id`: The id of your project in liara  This `WebSocket` endpoint allows `real-time` communication with the projects service hosted at `Liara` You can use `WebSocket protocols` to send and receive data, enabling efficient and low-latency interactions with the projects

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.deploy_api import DeployApi  # noqa: E501


class TestDeployApi(unittest.TestCase):
    """DeployApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeployApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_releases_deploy(self) -> None:
        """Test case for releases_deploy

        Deploy releases  # noqa: E501
        """
        pass

    def test_sources_deploy(self) -> None:
        """Test case for sources_deploy

        Deploy sources code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
