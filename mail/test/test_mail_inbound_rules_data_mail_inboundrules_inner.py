# coding: utf-8

"""
    Liara Mail API Documentaion

    A fully featured mail delivery platform for incoming & outgoing e-mail

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.mail_inbound_rules_data_mail_inboundrules_inner import MailInboundRulesDataMailInboundrulesInner  # noqa: E501

class TestMailInboundRulesDataMailInboundrulesInner(unittest.TestCase):
    """MailInboundRulesDataMailInboundrulesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MailInboundRulesDataMailInboundrulesInner:
        """Test MailInboundRulesDataMailInboundrulesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MailInboundRulesDataMailInboundrulesInner`
        """
        model = MailInboundRulesDataMailInboundrulesInner()  # noqa: E501
        if include_optional:
            return MailInboundRulesDataMailInboundrulesInner(
                created_at = '',
                rule = '',
                mail_server = ''
            )
        else:
            return MailInboundRulesDataMailInboundrulesInner(
        )
        """

    def testMailInboundRulesDataMailInboundrulesInner(self):
        """Test MailInboundRulesDataMailInboundrulesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
