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
from swagger_client.api.search_api import SearchApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_characters_character_id_search(self):
        """Test case for get_characters_character_id_search

        Search on a string  # noqa: E501
        """
        pass

    def test_get_search(self):
        """Test case for get_search

        Search on a string  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
