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
import datetime

from openapi_client.models.get_disk_backup import GetDiskBackup  # noqa: E501

class TestGetDiskBackup(unittest.TestCase):
    """GetDiskBackup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDiskBackup:
        """Test GetDiskBackup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDiskBackup`
        """
        model = GetDiskBackup()  # noqa: E501
        if include_optional:
            return GetDiskBackup(
                backups = [
                    openapi_client.models.get_disk_backup_backups_inner.Get_disk_backup_backups_inner(
                        name = '', 
                        last_modified = '', 
                        etag = '', 
                        size = 1.337, )
                    ]
            )
        else:
            return GetDiskBackup(
        )
        """

    def testGetDiskBackup(self):
        """Test GetDiskBackup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
