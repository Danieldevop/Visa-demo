# Receive Side Callback API
To facilitate the implementation of mVisa, Visa provides mVisa Receive Side API specifications to clients who implement a set of outbound RESTful APIs (Receive Side APIs) so that Visa can call these APIs to request clients to process the transactions over the Internet.

All URIs are relative to *https://sandbox.api.visa.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postcash_in**](ReceiveSideApi.md#postcash_in) | **POST** /visadirect/v1/pushpayment/transactions/receive/ci | 
[**postcash_in_0**](ReceiveSideApi.md#postcash_in_0) | **POST** /visadirect/v1/pushpayment/transactions/receive/co | 
[**postci_advice**](ReceiveSideApi.md#postci_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/ci | 
[**postco_advice**](ReceiveSideApi.md#postco_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/co | 
[**postreceive_p2_m**](ReceiveSideApi.md#postreceive_p2_m) | **POST** /visadirect/v1/pushpayment/transactions/receive/p2m | 
[**postreceive_p2_m_advice**](ReceiveSideApi.md#postreceive_p2_m_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/p2m | 


# **postcash_in**
> CashInpostResponse postcash_in(cash_inpost_payload)



Receive Cash-in API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postcash_in. Look at the documentation for further clarification.
cash_inpost_payload = src.CashInpostPayload() # CashInpostPayload | Request body for Receive Cash-In API

try: 
    api_response = api_instance.postcash_in(cash_inpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postcash_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_inpost_payload** | [**CashInpostPayload**](CashInpostPayload.md)| Request body for Receive Cash-In API | 

### Return type

[**CashInpostResponse**](CashInpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postcash_in_0**
> CashInpostResponse postcash_in_0(cash_inpost_payload)



Receive Cash-Out API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postcash_in_0. Look at the documentation for further clarification.
cash_inpost_payload = src.CashInpostPayload() # CashInpostPayload | Request body for Receive Cash-Out API

try: 
    api_response = api_instance.postcash_in_0(cash_inpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postcash_in_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_inpost_payload** | [**CashInpostPayload**](CashInpostPayload.md)| Request body for Receive Cash-Out API | 

### Return type

[**CashInpostResponse**](CashInpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postci_advice**
> CiAdvicepostResponse postci_advice(ci_advicepost_payload)



Receive Cash-in Advice API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postci_advice. Look at the documentation for further clarification.
ci_advicepost_payload = src.CiAdvicepostPayload() # CiAdvicepostPayload | Request body for Receive Cash-In Advice API

try: 
    api_response = api_instance.postci_advice(ci_advicepost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postci_advice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_advicepost_payload** | [**CiAdvicepostPayload**](CiAdvicepostPayload.md)| Request body for Receive Cash-In Advice API | 

### Return type

[**CiAdvicepostResponse**](CiAdvicepostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postco_advice**
> CoAdvicepostResponse postco_advice(co_advicepost_payload)



Receive Cash-out Advice API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postco_advice. Look at the documentation for further clarification.
co_advicepost_payload = src.CoAdvicepostPayload() # CoAdvicepostPayload | Request body for Receive Cash-Out Advice API

try: 
    api_response = api_instance.postco_advice(co_advicepost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postco_advice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **co_advicepost_payload** | [**CoAdvicepostPayload**](CoAdvicepostPayload.md)| Request body for Receive Cash-Out Advice API | 

### Return type

[**CoAdvicepostResponse**](CoAdvicepostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postreceive_p2_m**
> ReceiveP2MpostResponse postreceive_p2_m(receive_p2_mpost_payload)



Receive Person-to-Merchant API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postreceive_p2_m. Look at the documentation for further clarification.
receive_p2_mpost_payload = src.ReceiveP2MpostPayload() # ReceiveP2MpostPayload | Request body for Receive Person-to-Merchant API

try: 
    api_response = api_instance.postreceive_p2_m(receive_p2_mpost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postreceive_p2_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receive_p2_mpost_payload** | [**ReceiveP2MpostPayload**](ReceiveP2MpostPayload.md)| Request body for Receive Person-to-Merchant API | 

### Return type

[**ReceiveP2MpostResponse**](ReceiveP2MpostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)

# **postreceive_p2_m_advice**
> ReceiveP2MAdvicepostResponse postreceive_p2_m_advice(receive_p2_m_advicepost_payload)



Receive Person-to-Merchant Advice API specification

### Example 
```python
from __future__ import print_statement
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration
from pprint import pprint

config = Configuration()
# Uncomment this block to enable proxy
# config.proxy_url = 'PROXY_URL'

# Configure HTTP basic authorization: basicAuth
config.username = 'YOUR_USERNAME'
config.password = 'YOUR_PASSWORD'
config.cert_file = 'ABSOLUTE_PATH_TO_CERT_FILE'
config.key_file = 'ABSOLUTE_PATH_TO_KEY_FILE'
config.ssl_ca_cert = 'ABSOLUTE_PATH_TO_CA_CERT_FILE'

# Unblock this block to configure MLE credentials
# config.api_key['keyId'] = 'YOUR_KEY_ID'
# config.encryption_public_key_path = 'ABSOLUTE_PATH_TO_MLE_CERT_FILE'
# config.decryption_private_key_path = 'ABSOLUTE_PATH_TO_MLE_KEY_FILE'


# create an instance of the API class
api_instance = ReceiveSideApi()

# Set all the required parameters in the postreceive_p2_m_advice. Look at the documentation for further clarification.
receive_p2_m_advicepost_payload = src.ReceiveP2MAdvicepostPayload() # ReceiveP2MAdvicepostPayload | Request body for Receive Person-to-Merchant Advice API

try: 
    api_response = api_instance.postreceive_p2_m_advice(receive_p2_m_advicepost_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiveSideApi->postreceive_p2_m_advice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receive_p2_m_advicepost_payload** | [**ReceiveP2MAdvicepostPayload**](ReceiveP2MAdvicepostPayload.md)| Request body for Receive Person-to-Merchant Advice API | 

### Return type

[**ReceiveP2MAdvicepostResponse**](ReceiveP2MAdvicepostResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[Back to top](#)   |   [Back to API list](../README.md#documentation-for-api-endpoints)   |   [Back to Model list](../README.md#documentation-for-models)   |   [Back to README](../README.md)


##Authors
**Visa Developer Platform**
See also the list of [contributors](https://github.com/visa/java-sample-code/graphs/contributors) who participated in this project.

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