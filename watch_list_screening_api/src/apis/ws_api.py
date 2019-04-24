# coding: utf-8

"""
    Watch List Screening API

    The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists.  The Watch List Screening API also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re
import json

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()

        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def postwatchlistinquiry(self, watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, **kwargs):
        """
        Provide an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists. It also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.postwatchlistinquiry(watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload: Note: A unique value generated by the app that is used to tie together a WLM score request and WLM score response service calls. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload2: The name of the person who is to receive a WLM score. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload3:  (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload4: Note: This field is required if acquirerCountryCode field is provided.</br>The Bank Identification Number (BIN) under which your Fund Transfer is registered. This must match the information provided during enrollment. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload5: This is an optional field. If acquiringBin is provided, it is highly recommended that acquirerCountryCode is also provided.</br>Use a 3-digit numeric country code for the country where the Fund Transfer solution is registered. This must match the information provided during program enrollment. (required)
        :return: WatchlistinquirypostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.postwatchlistinquiry_with_http_info(watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, **kwargs)
        else:
            (data) = self.postwatchlistinquiry_with_http_info(watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, **kwargs)
            return data

    def postwatchlistinquiry_with_http_info(self, watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, **kwargs):
        """
        Provide an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists. It also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.postwatchlistinquiry_with_http_info(watchlistinquirypost_payload, watchlistinquirypost_payload2, watchlistinquirypost_payload3, watchlistinquirypost_payload4, watchlistinquirypost_payload5, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload: Note: A unique value generated by the app that is used to tie together a WLM score request and WLM score response service calls. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload2: The name of the person who is to receive a WLM score. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload3:  (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload4: Note: This field is required if acquirerCountryCode field is provided.</br>The Bank Identification Number (BIN) under which your Fund Transfer is registered. This must match the information provided during enrollment. (required)
        :param WatchlistinquirypostPayload watchlistinquirypost_payload5: This is an optional field. If acquiringBin is provided, it is highly recommended that acquirerCountryCode is also provided.</br>Use a 3-digit numeric country code for the country where the Fund Transfer solution is registered. This must match the information provided during program enrollment. (required)
        :return: WatchlistinquirypostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['watchlistinquirypost_payload', 'watchlistinquirypost_payload2', 'watchlistinquirypost_payload3', 'watchlistinquirypost_payload4', 'watchlistinquirypost_payload5']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postwatchlistinquiry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'watchlistinquirypost_payload' is set
        if ('watchlistinquirypost_payload' not in params) or (params['watchlistinquirypost_payload'] is None):
            raise ValueError("Missing the required parameter `watchlistinquirypost_payload` when calling `postwatchlistinquiry`")
        # verify the required parameter 'watchlistinquirypost_payload2' is set
        if ('watchlistinquirypost_payload2' not in params) or (params['watchlistinquirypost_payload2'] is None):
            raise ValueError("Missing the required parameter `watchlistinquirypost_payload2` when calling `postwatchlistinquiry`")
        # verify the required parameter 'watchlistinquirypost_payload3' is set
        if ('watchlistinquirypost_payload3' not in params) or (params['watchlistinquirypost_payload3'] is None):
            raise ValueError("Missing the required parameter `watchlistinquirypost_payload3` when calling `postwatchlistinquiry`")
        # verify the required parameter 'watchlistinquirypost_payload4' is set
        if ('watchlistinquirypost_payload4' not in params) or (params['watchlistinquirypost_payload4'] is None):
            raise ValueError("Missing the required parameter `watchlistinquirypost_payload4` when calling `postwatchlistinquiry`")
        # verify the required parameter 'watchlistinquirypost_payload5' is set
        if ('watchlistinquirypost_payload5' not in params) or (params['watchlistinquirypost_payload5'] is None):
            raise ValueError("Missing the required parameter `watchlistinquirypost_payload5` when calling `postwatchlistinquiry`")


        collection_formats = {}

        path = '/visadirect/watchlistscreening/v1/watchlistinquiry'.replace('{format}', 'json')
        resource_path = 'watchlistinquiry'
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'watchlistinquirypost_payload5' in params:
            body_params = params['watchlistinquirypost_payload5']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api(path, resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='WatchlistinquirypostResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

# ----------------------------------------------------------------------------------------------------------------------
# © Copyright 2018 Visa. All Rights Reserved.
#
# NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
# and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
# rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.
#
# By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy
# (developer.visa.com/privacy). In addition, all permissible uses of the Software must be in support of Visa products,
# programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com).
# THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL
# FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.
# ----------------------------------------------------------------------------------------------------------------------