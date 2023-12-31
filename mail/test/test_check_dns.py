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

from openapi_client.models.check_dns import CheckDNS  # noqa: E501

class TestCheckDNS(unittest.TestCase):
    """CheckDNS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckDNS:
        """Test CheckDNS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckDNS`
        """
        model = CheckDNS()  # noqa: E501
        if include_optional:
            return CheckDNS(
                status = '',
                data = openapi_client.models.check_dns_data.CheckDNS_data(
                    mail_server = openapi_client.models.check_dns_response.CheckDNSResponse(
                        dns_setup = openapi_client.models.check_dns_response_dns_setup.CheckDNSResponse_dns_setup(
                            dkim = openapi_client.models.check_dns_response_dns_setup_dkim.CheckDNSResponse_dns_setup_dkim(
                                dkim_error = '', 
                                dkim_record = '', 
                                dkim_record_name = '', 
                                dkim_status = '', ), 
                            mx_record = openapi_client.models.check_dns_response_dns_setup_mx_record.CheckDNSResponse_dns_setup_mx_record(
                                mx_error = '', 
                                mx_status = '', 
                                mx_record_value = '', ), 
                            return_path = openapi_client.models.check_dns_response_dns_setup_return_path.CheckDNSResponse_dns_setup_return_path(
                                return_path_domain = '', 
                                return_path_error = '', 
                                return_path_status = '', 
                                return_path_value = '', ), 
                            spf = openapi_client.models.check_dns_response_dns_setup_spf.CheckDNSResponse_dns_setup_spf(
                                spf_error = '', 
                                spf_record = '', 
                                spf_status = '', ), ), 
                        user = '', 
                        domain = '', 
                        records_status = '', 
                        mode = '', 
                        status = '', 
                        check_dns_record = True, 
                        created_at = '', 
                        updated_at = '', 
                        id = '', 
                        smtp_server = '', 
                        smtp_port = 1.337, ), )
            )
        else:
            return CheckDNS(
        )
        """

    def testCheckDNS(self):
        """Test CheckDNS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
