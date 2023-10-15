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

from openapi_client.models.get_ftps200_response_accesses_inner import GetFtps200ResponseAccessesInner  # noqa: E501

class TestGetFtps200ResponseAccessesInner(unittest.TestCase):
    """GetFtps200ResponseAccessesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFtps200ResponseAccessesInner:
        """Test GetFtps200ResponseAccessesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFtps200ResponseAccessesInner`
        """
        model = GetFtps200ResponseAccessesInner()  # noqa: E501
        if include_optional:
            return GetFtps200ResponseAccessesInner(
                id = '',
                disk = '',
                username = '',
                password = '',
                read_only = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                v = 56
            )
        else:
            return GetFtps200ResponseAccessesInner(
        )
        """

    def testGetFtps200ResponseAccessesInner(self):
        """Test GetFtps200ResponseAccessesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
