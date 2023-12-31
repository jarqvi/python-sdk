# coding: utf-8

"""
    DNS

    Manage dns zones and records

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.dns_record import DnsRecord  # noqa: E501

class TestDnsRecord(unittest.TestCase):
    """DnsRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsRecord:
        """Test DnsRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsRecord`
        """
        model = DnsRecord()  # noqa: E501
        if include_optional:
            return DnsRecord(
                name = '',
                type = '',
                ttl = 1.337,
                contents = [
                    None
                    ]
            )
        else:
            return DnsRecord(
        )
        """

    def testDnsRecord(self):
        """Test DnsRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
