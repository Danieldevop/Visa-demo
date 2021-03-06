# coding: utf-8

"""
    Mobile Push Payment Refund API

    Mobile Push Payment is a simple, secure and fast way to pay and be paid using mobile phones. Mobile Push Payment enables a range of payment use cases and is technology agnostic-leveraging evolving POS environment such as QR codes and works on both smart or feature phones.

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

from src.apis.refund_api_api import RefundApiApi
from src.configuration import Configuration
from globalConfig import GlobalConfig


class TestRefundApiApi(unittest.TestCase):
    """ RefundApiApi unit test stubs """

    @classmethod
    def setUpClass(self):
        print("---------------------------------------Tests---------------------------------------\nProduct Name: Visa Direct\nApi Name: Mobile Push Payment Refund API")
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
        self.api = RefundApiApi(None)

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
    Test case for getmerchandise_return_get

    .
    """
    def testgetmerchandise_return_get(self):
        print("\ngetmerchandise_return_get")
        result = self.api.getmerchandise_return_get(self.addRandom('random'))
        pass

    """
    Test case for getmerchandise_return_reversal_get

    .
    """
    def testgetmerchandise_return_reversal_get(self):
        print("\ngetmerchandise_return_reversal_get")
        result = self.api.getmerchandise_return_reversal_get(self.addRandom('random'))
        pass

    """
    Test case for postmerchandise_return_post

    .
    """
    def testpostmerchandise_return_post(self):
        print("\npostmerchandise_return_post")
        result = self.api.postmerchandise_return_post(self.transformPayload('{"localTransactionDateTime":"2018-10-09T15:46:10","recipientPrimaryAccountNumber":"4761360055652118","merchantCategoryCode":"6012","systemsTraceAuditNumber":"313223","transactionCurrencyCode":"USD","acquirerCountryCode":"643","cardAcceptor":{"idCode":"ID-Code123","name":"CA123","address":{"country":"IND","city":"Bangalore"}},"acquiringBin":"400171","retrievalReferenceNumber":"430000367722","amount":"124.05"}'))
        pass

    """
    Test case for postmerchandise_return_reversal_post

    .
    """
    def testpostmerchandise_return_reversal_post(self):
        print("\npostmerchandise_return_reversal_post")
        result = self.api.postmerchandise_return_reversal_post(self.transformPayload('{"localTransactionDateTime":"2016-12-12T21:32:52","acquiringBin":"830","feeProgramIndicator":"aaa","transactionFeeAmt":"2","merchantVerificationValue":{"mvvAcquirerAssigned":"41394644363445313243","mvvVisaAssigned":"41394644363445313243"},"acquirerCountryCode":"101","transactionIdentifier":"381228649430011","cardAcceptor":{"idCode":"VMT200911026070","address":{"county":"kolkata","country":"IND","state":"KO","zipCode":"94404"},"terminalId":"365539","name":"Visa Inc. USA-Foster City"},"originalDataElements":{"acquiringBin":"408999","systemsTraceAuditNumber":"897825","approvalCode":"20304B","transmissionDateTime":"2016-11-30T03:00:37"},"recipientPrimaryAccountNumber":"4898100000000245","retrievalReferenceNumber":"330000550000","systemsTraceAuditNumber":"451050","senderCurrencyCode":"USD","amount":"24.01"}'))
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