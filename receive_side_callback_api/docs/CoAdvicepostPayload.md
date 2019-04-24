# CoAdvicepostPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_transaction_time** | **str** | The time the transaction takes place, expressed in the local time of the originator. The time is in hhmmss format. | 
**visa_transaction_id** | **str** | Numeric. It contains a right-justified, VisaNet generated Transaction Identifier (TID) that is unique for each request. The identifier links original messages to subsequent messages, such as those for exception item processing and clearing record. | 
**originator_country_code** | **str** | A 3-digit ISO-4217 code that identifies the country of the originating BIN.&lt;br&gt;Refer to &lt;a href&#x3D;\&quot;/request_response_codes#iso_country_codes\&quot;&gt;ISO codes&lt;/a&gt;. | 
**decimal_position_indicator** | **str** | Indicates the number of decimal positions following the amount field. This field is to be sent as NULL if it is not populated. | 
**retrieval_reference_number** | **str** | Numeric. It is a key data element for matching a message to others within a given transaction set. The same number appears in all related messages: response, advice, reversal, chargeback, chargeback reversal, or representment. The format is recommended to be &lt;b&gt;ydddhhnnnnnn&lt;/b&gt;. | 
**velocity_limit_indicator** | **str** | &lt;b&gt;Conditional&lt;/b&gt;. This field contains the velocity limit related information that Acquirer can use in making the authorization decision:&lt;ul&gt;&lt;li&gt;1 &#x3D; 1-day count or amount exceeded.&lt;/li&gt;&lt;li&gt;2 &#x3D; 7-day count or amount exceeded.&lt;/li&gt;&lt;li&gt;3 &#x3D; 30-day count or amount exceeded.&lt;/li&gt;&lt;/ul&gt;The field is populated with priority of 1, 2 and then 3.&lt;br&gt;This field is sent if recipient has opted for VisaNet to forward them the OCT when a velocity limit has been exceeded.&lt;br&gt;This field will be sent as NULL if it is not populated. | [optional] 
**agent_country_code** | **str** | &lt;b&gt;Conditional&lt;/b&gt;. Recipient may replace this field with 2-letter ISO 3166 country code of the agent, if different than the value provided by the originator. Visa settlement reports would contain the value provided by recipient. This field is to be sent as NULL if it is not populated. | [optional] 
**enc_consumer_name** | **str** | Consumer name. If consumer name is greater than 30 characters, then only first 30 characters will be expected. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). | 
**message_type** | **str** | Possible values based on Message Type Identifier are:&lt;br&gt;&lt;ul&gt;&lt;li&gt;0200 : &#39;Recipient Timeout&#39;&lt;/li&gt;&lt;li&gt;0220 : &#39;Advice&#39; (STIP decline advice)&lt;/li&gt;&lt;li&gt;0210 : &#39;Reject&#39; (VIP reject)&lt;/li&gt;&lt;/ul&gt; | 
**rejection_code** | **str** | Only populated if Advice message type is ‘Reject’. This field contains the VisaNet rejection code. | 
**local_transaction_date** | **str** | It contains the local month and day on which the transaction was originated. The date is in mmdd format. | 
**enc_agent_pan** | **str** | Agent PAN. 16-digit PAN as created from the mVisa agent ID captured by the consumer from agent information display option. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption. | 
**originator_bin** | **str** | This BIN number identifies the originator of Cash-Out payment transaction. | 
**system_trace_audit_number** | **str** | Numeric. It is a key data element used to match a response to its request or to match a message to others for a given transaction. | 
**response_code** | **str** | Contains a code (also known as &#39;Action Code&#39;) that defines the response to a request. Refer to actionCode | 
**transaction_currency_code** | **str** | The 3-digit ISO-4217 code in this field reflects the currency associated to the transactionAmount field. | 
**enc_consumer_pan** | **str** | Consumer PAN. This is a 16-digit PAN. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption. | [optional] 
**agent_city** | **str** | Agent city name. | 
**transaction_amount** | **str** | Transaction amount in agent on currency. In case the agent currency is not the same as the consumer currency, then originator will perform currency conversion before submitting the transaction. | 
**auth_id_response** | **str** | Contains the authorization code provided by the recipient when a transaction is approved. Visa recommends that recipient maintains uniqueness of this code for a given merchant PAN, however Visa would not maintain any checks for uniqueness. This field is to be sent as NULL if it is not populated. | [optional] 
**transmission_date_time** | **str** | The date and time the request was submitted to Visa. Format: MMDDhhmmss. | 

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