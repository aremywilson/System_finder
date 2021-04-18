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
from swagger_client.api.alliance_api import AllianceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAllianceApi(unittest.TestCase):
    """AllianceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.alliance_api.AllianceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_alliances(self):
        """Test case for get_alliances

        List all alliances  # noqa: E501
        """
        pass

    def test_get_alliances_alliance_id(self):
        """Test case for get_alliances_alliance_id

        Get alliance information  # noqa: E501
        """
        pass

    def test_get_alliances_alliance_id_corporations(self):
        """Test case for get_alliances_alliance_id_corporations

        List alliance's corporations  # noqa: E501
        """
        pass

    def test_get_alliances_alliance_id_icons(self):
        """Test case for get_alliances_alliance_id_icons

        Get alliance icon  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
