# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sovereignty_api import SovereigntyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSovereigntyApi(unittest.TestCase):
    """SovereigntyApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sovereignty_api.SovereigntyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sovereignty_campaigns(self):
        """Test case for get_sovereignty_campaigns

        List sovereignty campaigns  # noqa: E501
        """
        pass

    def test_get_sovereignty_map(self):
        """Test case for get_sovereignty_map

        List sovereignty of systems  # noqa: E501
        """
        pass

    def test_get_sovereignty_structures(self):
        """Test case for get_sovereignty_structures

        List sovereignty structures  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()