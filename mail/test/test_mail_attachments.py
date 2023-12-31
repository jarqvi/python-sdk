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

from openapi_client.models.mail_attachments import MailAttachments  # noqa: E501

class TestMailAttachments(unittest.TestCase):
    """MailAttachments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MailAttachments:
        """Test MailAttachments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MailAttachments`
        """
        model = MailAttachments()  # noqa: E501
        if include_optional:
            return MailAttachments(
                status = '',
                data = openapi_client.models.mail_attachments_data.MailAttachments_data(
                    attachments = [
                        openapi_client.models.mail_attachment.MailAttachment(
                            name = '', 
                            size = 1.337, 
                            content_type = '', 
                            created_at = '', 
                            id = '', 
                            data = '', )
                        ], )
            )
        else:
            return MailAttachments(
        )
        """

    def testMailAttachments(self):
        """Test MailAttachments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
