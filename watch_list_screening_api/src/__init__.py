# coding: utf-8

"""
    Watch List Screening API

    The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists.  The Watch List Screening API also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.watchlistinquirypost_payload import WatchlistinquirypostPayload
from .models.watchlistinquirypost_response import WatchlistinquirypostResponse

# import apis into sdk package
from .apis.ws_api import WsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()

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