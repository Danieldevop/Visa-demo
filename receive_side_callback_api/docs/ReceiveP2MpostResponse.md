# ReceiveP2MpostResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_city** | **str** | This is called Card Acceptor Location. Recipient must replace this field with the city name of Merchant. Visa settlement reports would contain the value provided by recipient.&lt;br&gt;If encounter errors or the merchant PAN is invalid/does not belong to the acquirer, the acquirer should send HTTP 200 with decline response code and echo back the same field content sent in the request. | 
**merchant_category_code** | **str** | Recipient should populate the Merchant Category Code (MCC) of the merchant in the response message. If replaced by recipient Visa settlement reports would contain the value provided by recipient. This field accepts only numeric data. If there is non numeric data provided in this field the default &#39;0000&#39; translation will be sent to VisaNet.&lt;br&gt;If encounter errors or the merchant PAN is invalid/does not belong to the acquirer, the acquirer should send HTTP 200 with decline response code and echo back the same field content sent in the request. | 
**fee_program_indicator** | **str** | Optional field which may be populated by recipient where applicable. This field is to be sent as NULL if it is not populated. | [optional] 
**merchant_name** | **str** | This is called Card Acceptor Name in the VisaNet Specifications. Recipient must replace this field with the ‘doing business as’ name of Merchant. Visa settlement reports would contain the value provided by recipient.&lt;br&gt;If encounter errors or the merchant PAN is invalid/does not belong to the acquirer, the acquirer should send HTTP 200 with decline response code and echo back the same field content sent in the request. | 
**receiver_transaction_id** | **str** | Acquirer may provide a transaction ID that can be used for investigation if required. This field is to be sent as NULL if it is not populated | [optional] 
**merchant_verification_value** | **str** | Recipient are expected to populate the Merchant Verification Value used to identify merchants that participate in a variety of programs in this field. This field is to be sent as NULL if it is not populated. | [optional] 
**merchant_terminal_id** | **str** | &lt;b&gt;Conditional&lt;/b&gt;. Recipient may replace this field with card acceptor terminal ID as defined in recipient system. If replaced by recipient, all occurrences of card acceptor terminal ID in reports, files, transaction inquiries, etc. will contain the value provided by the recipient. This field is to be sent as NULL if it is not populated. | [optional] 
**merchant_country_code** | **str** | &lt;b&gt;Conditional&lt;/b&gt;. Recipient may replace this field with the 2-letter ISO 3166 country code of the merchant, if the country code of recipient is different than originator. Visa settlement reports would contain the value provided by recipient. This field is to be sent as NULL if it is not populated. | [optional] 
**response_code** | **str** | Contains a code (also known as &#39;Action Code&#39;) that defines the response to a request. Refer to actionCode | 
**merchant_id** | **str** | &lt;b&gt;Conditional&lt;/b&gt;. Recipient may replace this field with card acceptor ID code of the merchant as defined in recipient system. If replaced by recipient, all occurrences of card acceptor ID code in reports, files, transaction inquiries, etc. will contain the value provided by the recipient. This field is to be sent as NULL if it is not populated. | [optional] 
**auth_id_response** | **str** | Contains the authorization code provided by the recipient when a transaction is approved. Visa recommends that recipient maintains uniqueness of this code for a given merchant PAN, however Visa would not maintain any checks for uniqueness. This field is to be sent as NULL if it is not populated. | [optional] 

[Back to Model list](../README.md#documentation-for-models)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to README](../README.md)



##License
**© Copyright 2018 Visa. All Rights Reserved.**

*NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*

*By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).
In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided
through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED
INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR
CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply
product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally
do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims
all liability for any such components, including continued availability and functionality. Benefits depend on implementation
details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the
described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,
implementation and resources by you based on your business and operational details. Please refer to the specific
API documentation for details on the requirements, eligibility and geographic availability.*

*This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,
functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.
The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,
including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*