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

from openapi_client.api.disks_api import DisksApi  # noqa: E501


class TestDisksApi(unittest.TestCase):
    """DisksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DisksApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_backup(self) -> None:
        """Test case for create_backup

        Create backup disk  # noqa: E501
        """
        pass

    def test_create_disk(self) -> None:
        """Test case for create_disk

        Create a disk  # noqa: E501
        """
        pass

    def test_create_ftp(self) -> None:
        """Test case for create_ftp

        Create ftp  # noqa: E501
        """
        pass

    def test_delete_disk(self) -> None:
        """Test case for delete_disk

        Delete a disk  # noqa: E501
        """
        pass

    def test_delete_ftp(self) -> None:
        """Test case for delete_ftp

        Delete a ftp  # noqa: E501
        """
        pass

    def test_download_backup(self) -> None:
        """Test case for download_backup

        Download backup disk  # noqa: E501
        """
        pass

    def test_get_backups(self) -> None:
        """Test case for get_backups

        Get backups disk  # noqa: E501
        """
        pass

    def test_get_disks(self) -> None:
        """Test case for get_disks

        Get disks  # noqa: E501
        """
        pass

    def test_get_ftps(self) -> None:
        """Test case for get_ftps

        Get ftps  # noqa: E501
        """
        pass

    def test_resize_disk(self) -> None:
        """Test case for resize_disk

        Resize disk  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
