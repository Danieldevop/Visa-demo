# coding: utf-8

"""
    Watch List Screening API

    The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists.  The Watch List Screening API also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest
import datetime
import pytz
import random
import string
import re
import json

from src.apis.ws_api import WsApi
from src.configuration import Configuration
from globalConfig import GlobalConfig


class TestWsApi(unittest.TestCase):
    """ WsApi unit test stubs """

    @classmethod
    def setUpClass(self):
        print("---------------------------------------Tests---------------------------------------\nProduct Name: Visa Direct\nApi Name: Watch List Screening API")
        globalConfig = GlobalConfig()
        config = Configuration()
        config.username = globalConfig.userName
        config.password = globalConfig.password
        config.cert_file = globalConfig.certificatePath
        config.key_file = globalConfig.privateKeyPath
        config.shared_secret = globalConfig.sharedSecret
        config.api_key['apikey'] = globalConfig.apiKey
        config.ssl_ca_cert = globalConfig.caCertPath
        config.proxy_url = globalConfig.proxyUrl
        self.api = WsApi(None)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def transformPayload(self, payload):
        payload = self.editLocalTime(payload)
        payload = self.addRandom(payload)
        payload = json.loads(payload)
        return payload

    def editLocalTime(self, payload):
        timezone = pytz.timezone("America/Los_Angeles")
        timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
        pattern = re.compile('"localTransactionDateTime":".{19}"', re.IGNORECASE)
        replacement = '"localTransactionDateTime": "'+timestamp+'"'
        payload = re.sub(pattern, replacement, payload)

        timestamp = timezone.localize(datetime.datetime.now()).strftime('%m%d%H%M%S')
        pattern = re.compile('"dateTimeLocal":".{10}"', re.IGNORECASE)
        replacement = '"dateTimeLocal": "'+timestamp+'"'
        payload = re.sub(pattern, replacement, payload)
        return payload

    def addRandom(self, payload):
        if payload == 'mle_keyId':
            return self.mleKeyId
        payload = re.sub(r'random_string', ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)), payload)
        payload = re.sub(r'random_integer', ''.join(random.choice(string.digits) for _ in range(8)), payload)
        payload= re.sub(r'random', ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)), payload)
        return payload

    """
    Test case for postwatchlistinquiry

    .
    """
    def testpostwatchlistinquiry(self):
        print("\npostwatchlistinquiry")
        result = self.api.postwatchlistinquiry(self.transformPayload('{"acquiringBin":"408999","address":{"city":"San Francisco","cardIssuerCountryCode":"USA"},"acquirerCountryCode":"840","name":"Mohammed Qasim","referenceNumber":"330000550000"}'), self.transformPayload('{"acquiringBin":"408999","address":{"city":"San Francisco","cardIssuerCountryCode":"USA"},"acquirerCountryCode":"840","name":"Mohammed Qasim","referenceNumber":"330000550000"}'), self.transformPayload('{"acquiringBin":"408999","address":{"city":"San Francisco","cardIssuerCountryCode":"USA"},"acquirerCountryCode":"840","name":"Mohammed Qasim","referenceNumber":"330000550000"}'), self.transformPayload('{"acquiringBin":"408999","address":{"city":"San Francisco","cardIssuerCountryCode":"USA"},"acquirerCountryCode":"840","name":"Mohammed Qasim","referenceNumber":"330000550000"}'), self.transformPayload('{"acquiringBin":"408999","address":{"city":"San Francisco","cardIssuerCountryCode":"USA"},"acquirerCountryCode":"840","name":"Mohammed Qasim","referenceNumber":"330000550000"}'))
        pass


if __name__ == '__main__':
    unittest.main()


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