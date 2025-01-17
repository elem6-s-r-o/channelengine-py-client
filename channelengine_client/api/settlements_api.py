# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channelengine_client.api_client import ApiClient


class SettlementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def settlement_get_by_filter(self, **kwargs):  # noqa: E501
        """Gets settlements  # noqa: E501

        Gets the settlements based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settlement_get_by_filter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool un_exported_only: Filter on settlements that have not been exported before.
        :param list[int] settlement_ids: Filter on settlement IDs.
        :param list[str] channel_settlement_nos: Filter on channel settlement nos.
        :param list[int] channel_ids: Filter on channel id list.
        :param datetime from_start_date: Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime to_start_date: Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_end_date: Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive.
        :param datetime to_end_date: Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_create_date: Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime to_create_date: Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_update_date: Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive.
        :param datetime to_update_date: Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantSettlementReportsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settlement_get_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.settlement_get_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def settlement_get_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Gets settlements  # noqa: E501

        Gets the settlements based on the available filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settlement_get_by_filter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool un_exported_only: Filter on settlements that have not been exported before.
        :param list[int] settlement_ids: Filter on settlement IDs.
        :param list[str] channel_settlement_nos: Filter on channel settlement nos.
        :param list[int] channel_ids: Filter on channel id list.
        :param datetime from_start_date: Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime to_start_date: Filter on the start date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_end_date: Filter on the end date of the settlement in ChannelEngine, starting from this date. This date is inclusive.
        :param datetime to_end_date: Filter on the end date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_create_date: Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime to_create_date: Filter on the create date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param datetime from_update_date: Filter on the update date of the settlement in ChannelEngine, starting from this date. This date is inclusive.
        :param datetime to_update_date: Filter on the update date of the settlement in ChannelEngine, until this date. This date is exclusive.
        :param int page: The page to filter on. Starts at 1.
        :return: CollectionOfMerchantSettlementReportsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['un_exported_only', 'settlement_ids', 'channel_settlement_nos', 'channel_ids', 'from_start_date', 'to_start_date', 'from_end_date', 'to_end_date', 'from_create_date', 'to_create_date', 'from_update_date', 'to_update_date', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settlement_get_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'un_exported_only' in params:
            query_params.append(('unExportedOnly', params['un_exported_only']))  # noqa: E501
        if 'settlement_ids' in params:
            query_params.append(('settlementIds', params['settlement_ids']))  # noqa: E501
            collection_formats['settlementIds'] = 'multi'  # noqa: E501
        if 'channel_settlement_nos' in params:
            query_params.append(('channelSettlementNos', params['channel_settlement_nos']))  # noqa: E501
            collection_formats['channelSettlementNos'] = 'multi'  # noqa: E501
        if 'channel_ids' in params:
            query_params.append(('channelIds', params['channel_ids']))  # noqa: E501
            collection_formats['channelIds'] = 'multi'  # noqa: E501
        if 'from_start_date' in params:
            query_params.append(('fromStartDate', params['from_start_date']))  # noqa: E501
        if 'to_start_date' in params:
            query_params.append(('toStartDate', params['to_start_date']))  # noqa: E501
        if 'from_end_date' in params:
            query_params.append(('fromEndDate', params['from_end_date']))  # noqa: E501
        if 'to_end_date' in params:
            query_params.append(('toEndDate', params['to_end_date']))  # noqa: E501
        if 'from_create_date' in params:
            query_params.append(('fromCreateDate', params['from_create_date']))  # noqa: E501
        if 'to_create_date' in params:
            query_params.append(('toCreateDate', params['to_create_date']))  # noqa: E501
        if 'from_update_date' in params:
            query_params.append(('fromUpdateDate', params['from_update_date']))  # noqa: E501
        if 'to_update_date' in params:
            query_params.append(('toUpdateDate', params['to_update_date']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/settlements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionOfMerchantSettlementReportsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def settlement_upload_settlement(self, **kwargs):  # noqa: E501
        """Uploads a settlement file to ChannelEngine.  # noqa: E501

        Uploads a settlement file to ChannelEngine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settlement_upload_settlement(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str settlement:
        :param int channel_id: The channel ID of the channel which the settlement is for.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settlement_upload_settlement_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.settlement_upload_settlement_with_http_info(**kwargs)  # noqa: E501
            return data

    def settlement_upload_settlement_with_http_info(self, **kwargs):  # noqa: E501
        """Uploads a settlement file to ChannelEngine.  # noqa: E501

        Uploads a settlement file to ChannelEngine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settlement_upload_settlement_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str settlement:
        :param int channel_id: The channel ID of the channel which the settlement is for.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settlement', 'channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settlement_upload_settlement" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in params:
            query_params.append(('channelId', params['channel_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'settlement' in params:
            local_var_files['settlement'] = params['settlement']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/settlements/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
