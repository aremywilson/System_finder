# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.7.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AllianceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_alliances(self, **kwargs):  # noqa: E501
        """List all alliances  # noqa: E501

        List all active player alliances  --- Alternate route: `/dev/alliances/`  Alternate route: `/legacy/alliances/`  Alternate route: `/v1/alliances/`  Alternate route: `/v2/alliances/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alliances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_alliances_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_alliances_with_http_info(self, **kwargs):  # noqa: E501
        """List all alliances  # noqa: E501

        List all active player alliances  --- Alternate route: `/dev/alliances/`  Alternate route: `/legacy/alliances/`  Alternate route: `/v1/alliances/`  Alternate route: `/v2/alliances/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alliances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alliances/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alliances_alliance_id(self, alliance_id, **kwargs):  # noqa: E501
        """Get alliance information  # noqa: E501

        Public information about an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/`  Alternate route: `/legacy/alliances/{alliance_id}/`  Alternate route: `/v3/alliances/{alliance_id}/`  Alternate route: `/v4/alliances/{alliance_id}/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alliances_alliance_id_with_http_info(alliance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alliances_alliance_id_with_http_info(alliance_id, **kwargs)  # noqa: E501
            return data

    def get_alliances_alliance_id_with_http_info(self, alliance_id, **kwargs):  # noqa: E501
        """Get alliance information  # noqa: E501

        Public information about an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/`  Alternate route: `/legacy/alliances/{alliance_id}/`  Alternate route: `/v3/alliances/{alliance_id}/`  Alternate route: `/v4/alliances/{alliance_id}/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id_with_http_info(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alliance_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alliances_alliance_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alliance_id' is set
        if self.api_client.client_side_validation and ('alliance_id' not in params or
                                                       params['alliance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `alliance_id` when calling `get_alliances_alliance_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('alliance_id' in params and params['alliance_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `alliance_id` when calling `get_alliances_alliance_id`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'alliance_id' in params:
            path_params['alliance_id'] = params['alliance_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alliances/{alliance_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alliances_alliance_id_corporations(self, alliance_id, **kwargs):  # noqa: E501
        """List alliance's corporations  # noqa: E501

        List all current member corporations of an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/corporations/`  Alternate route: `/legacy/alliances/{alliance_id}/corporations/`  Alternate route: `/v1/alliances/{alliance_id}/corporations/`  Alternate route: `/v2/alliances/{alliance_id}/corporations/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id_corporations(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alliances_alliance_id_corporations_with_http_info(alliance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alliances_alliance_id_corporations_with_http_info(alliance_id, **kwargs)  # noqa: E501
            return data

    def get_alliances_alliance_id_corporations_with_http_info(self, alliance_id, **kwargs):  # noqa: E501
        """List alliance's corporations  # noqa: E501

        List all current member corporations of an alliance  --- Alternate route: `/dev/alliances/{alliance_id}/corporations/`  Alternate route: `/legacy/alliances/{alliance_id}/corporations/`  Alternate route: `/v1/alliances/{alliance_id}/corporations/`  Alternate route: `/v2/alliances/{alliance_id}/corporations/`  --- This route is cached for up to 3600 seconds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id_corporations_with_http_info(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alliance_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alliances_alliance_id_corporations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alliance_id' is set
        if self.api_client.client_side_validation and ('alliance_id' not in params or
                                                       params['alliance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `alliance_id` when calling `get_alliances_alliance_id_corporations`")  # noqa: E501

        if self.api_client.client_side_validation and ('alliance_id' in params and params['alliance_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `alliance_id` when calling `get_alliances_alliance_id_corporations`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'alliance_id' in params:
            path_params['alliance_id'] = params['alliance_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alliances/{alliance_id}/corporations/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alliances_alliance_id_icons(self, alliance_id, **kwargs):  # noqa: E501
        """Get alliance icon  # noqa: E501

        Get the icon urls for a alliance  --- Alternate route: `/legacy/alliances/{alliance_id}/icons/`  Alternate route: `/v1/alliances/{alliance_id}/icons/`  --- This route expires daily at 11:05  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/alliances/{alliance_id}/icons/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id_icons(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alliances_alliance_id_icons_with_http_info(alliance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alliances_alliance_id_icons_with_http_info(alliance_id, **kwargs)  # noqa: E501
            return data

    def get_alliances_alliance_id_icons_with_http_info(self, alliance_id, **kwargs):  # noqa: E501
        """Get alliance icon  # noqa: E501

        Get the icon urls for a alliance  --- Alternate route: `/legacy/alliances/{alliance_id}/icons/`  Alternate route: `/v1/alliances/{alliance_id}/icons/`  --- This route expires daily at 11:05  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/alliances/{alliance_id}/icons/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alliances_alliance_id_icons_with_http_info(alliance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int alliance_id: An EVE alliance ID (required)
        :param str datasource: The server name you would like data from
        :param str if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alliance_id', 'datasource', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alliances_alliance_id_icons" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alliance_id' is set
        if self.api_client.client_side_validation and ('alliance_id' not in params or
                                                       params['alliance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `alliance_id` when calling `get_alliances_alliance_id_icons`")  # noqa: E501

        if self.api_client.client_side_validation and ('alliance_id' in params and params['alliance_id'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `alliance_id` when calling `get_alliances_alliance_id_icons`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'alliance_id' in params:
            path_params['alliance_id'] = params['alliance_id']  # noqa: E501

        query_params = []
        if 'datasource' in params:
            query_params.append(('datasource', params['datasource']))  # noqa: E501

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/alliances/{alliance_id}/icons/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
