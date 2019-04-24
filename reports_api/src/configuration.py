# coding: utf-8

"""
    Reports API

    The Reports API provides reporting capabilities such as transaction reconciliation data API. The data needed for reconciliation includes both push(OCT) and pull(AFT) transaction details and any exceptions such as chargebacks & reversals. This data allows you to reconcile the transactions sent by your systems with what was processed through VisaNet.<br> <br> <b>Note: This functionality is currently available for US transactions ONLY.</b>

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import urllib3

import sys
import logging

from six import iteritems
from six.moves import http_client as httplib
import datetime
import calendar
import hmac
import hashlib

def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Configuration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Constructor
        """
        # Default Base url
        self.host = "https://sandbox.api.visa.com"
        # Default api client
        self.api_client = None
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = {}
        # dict to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}
        # Username for HTTP basic authentication
        self.username = ""
        # Password for HTTP basic authentication
        self.password = ""
        # shared secret (for XPay Token auth)
        self.shared_secret = None

        # Encryption public key path
        self.encryption_public_key_path = ""
        # Decryption private key path
        self.decryption_private_key_path = ""


        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("src")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # proxy url
        self.proxy_url = None


    @property
    def logger_file(self):
        """
        Gets the logger_file.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """
        Sets the logger_file.

        If the logger_file is None, then add stream handler and remove file handler.
        Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """
        Gets the debug status.
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """
        Sets the debug status.

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """
        Gets the logger_format.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """
        Sets the logger_format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, query_params, resource_path, body):
        """
        Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :return: The token for api key authentication.
        """
        if identifier == 'x-pay-token':
            return self.get_x_pay_token(query_params, resource_path, body)

        if self.api_key.get(identifier) and self.api_key_prefix.get(identifier):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """
        Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        return urllib3.util.make_headers(basic_auth=self.username + ':' + self.password)\
                           .get('authorization')

    def _get_timestamp(self):
        d = datetime.datetime.utcnow()
        timestamp = calendar.timegm(d.timetuple())
        return str(timestamp)

    def get_x_pay_token(self, query_params, resource_path, body):
        """
        Gets XPay Token header
        """
        query_params = sorted(query_params, key=lambda x: x[0])
        if body == 'null':
            body = ''
        shared_secret = self.shared_secret
        query_string = ''
        timestamp = self._get_timestamp()
        for idx, tuple in enumerate(query_params):
            if idx > 0:
                query_string += '&'
            query_string += tuple[0] + '=' + tuple[1]
        pre_hash_string = timestamp + resource_path + query_string + body

        if sys.version_info < (3, 0):
            hash_string = hmac.new(shared_secret, msg=pre_hash_string.rstrip(), digestmod=hashlib.sha256).hexdigest()
        else:
            hash_string = hmac.new(str.encode(shared_secret), msg=pre_hash_string.rstrip().encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
        return 'xv2:' + timestamp + ':' + hash_string


    def auth_settings(self, auth_method, query_params, resource_path, body):
        """
        Gets Auth Settings dict for api client.
        :param resource_path: Resource path for the endpoint. Needed for XPayToken

        :return: The Auth Settings information dict.
        """
        if auth_method == 'basicAuth':
            return {
                'type': 'basic',
                'in': 'header',
                'key': 'Authorization',
                'value': self.get_basic_auth_token()
            }


    def to_debug_report(self):
        """
        Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: v1\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def _get_timestamp(self):
        d = datetime.datetime.utcnow()
        timestamp = calendar.timegm(d.timetuple())
        return str(timestamp)


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