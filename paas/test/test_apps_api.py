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

from openapi_client.api.apps_api import AppsApi  # noqa: E501


class TestAppsApi(unittest.TestCase):
    """AppsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AppsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_change_plan(self) -> None:
        """Test case for change_plan

        Change plan  # noqa: E501
        """
        pass

    def test_create_app(self) -> None:
        """Test case for create_app

        Create a app  # noqa: E501
        """
        pass

    def test_delete_app_by_name(self) -> None:
        """Test case for delete_app_by_name

        Delete a app  # noqa: E501
        """
        pass

    def test_get_app_applets(self) -> None:
        """Test case for get_app_applets

        Get applets of app  # noqa: E501
        """
        pass

    def test_get_app_by_name(self) -> None:
        """Test case for get_app_by_name

        Get details of a project  # noqa: E501
        """
        pass

    def test_get_app_logs(self) -> None:
        """Test case for get_app_logs

        Get logs of app  # noqa: E501
        """
        pass

    def test_get_app_releases(self) -> None:
        """Test case for get_app_releases

        Get releases of app  # noqa: E501
        """
        pass

    def test_get_apps(self) -> None:
        """Test case for get_apps

        Get details of all projects  # noqa: E501
        """
        pass

    def test_restart_app(self) -> None:
        """Test case for restart_app

        To restart a app  # noqa: E501
        """
        pass

    def test_turn_app(self) -> None:
        """Test case for turn_app

        Turn on or off a app  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
