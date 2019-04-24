# Receive Side Callback API
To facilitate the implementation of mVisa, Visa provides mVisa Receive Side API specifications to clients who implement a set of outbound RESTful APIs (Receive Side APIs) so that Visa can call these APIs to request clients to process the transactions over the Internet.

- API version: 1.0
- Package version: 1.0.0

For more information, please visit [https://developer.visa.com/](https://developer.visa.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

To install by pip, execute the below command.

```sh
pip install -r requirements.txt
```
(you may need to run `pip` with root permission: `sudo pip install -r requirements.txt`)

Then import the package:
```python
from src.apis.receive_side_api import ReceiveSideApi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
from src.apis.receive_side_api import ReceiveSideApi
```
## Tests
- Edit the file **globlaConfig.py** to set the fields shown below. Please refer the [Getting Started Guide](https://developer.visa.com/vdpguide#get-started-overview) to get the credentials.

```python
# For mutual auth
userName = 'your_username'
password = 'your_password'
certificatePath = '/absolute/path/to/cert.pem'
privateKeyPath = '/absolute/path/to/key_xxxx.pem'
caCertPath = '/absolute/path/to/cacert.pem'

# For MLE also set the following fields
mleKeyId = 'your_keyId'
encryptionPublicKeyPath = 'your_encryption_public_key_path'
self.decryptionPrivateKeyPath = 'your_decryption_private_key_path'

# For x-pay token
apiKey = 'your_apiKey'
sharedSecret = 'your_shared_secret'

# For Proxy
proxyUrl = 'proxy_url'

```
To run the unit tests:
- Note: The data in the unit tests are just placeholders. Please refer the [Create Project Guide](https://developer.visa.com/pages/working-with-visa-apis/create-project) to get the test data
```
nosetests --nocapture
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
from src.apis.receive_side_api import ReceiveSideApi
from src.configuration import Configuration

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

## Documentation for API Endpoints

All URIs are relative to *https://sandbox.api.visa.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ReceiveSideApi* | [**postcash_in**](docs/ReceiveSideApi.md#postcash_in) | **POST** /visadirect/v1/pushpayment/transactions/receive/ci | 
*ReceiveSideApi* | [**postcash_in_0**](docs/ReceiveSideApi.md#postcash_in_0) | **POST** /visadirect/v1/pushpayment/transactions/receive/co | 
*ReceiveSideApi* | [**postci_advice**](docs/ReceiveSideApi.md#postci_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/ci | 
*ReceiveSideApi* | [**postco_advice**](docs/ReceiveSideApi.md#postco_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/co | 
*ReceiveSideApi* | [**postreceive_p2_m**](docs/ReceiveSideApi.md#postreceive_p2_m) | **POST** /visadirect/v1/pushpayment/transactions/receive/p2m | 
*ReceiveSideApi* | [**postreceive_p2_m_advice**](docs/ReceiveSideApi.md#postreceive_p2_m_advice) | **POST** /visadirect/v1/pushpayment/advice/receive/p2m | 


## Documentation For Models

 - [CashInpostPayload](docs/CashInpostPayload.md)
 - [CashInpostResponse](docs/CashInpostResponse.md)
 - [CiAdvicepostPayload](docs/CiAdvicepostPayload.md)
 - [CiAdvicepostResponse](docs/CiAdvicepostResponse.md)
 - [CoAdvicepostPayload](docs/CoAdvicepostPayload.md)
 - [CoAdvicepostResponse](docs/CoAdvicepostResponse.md)
 - [ReceiveP2MAdvicepostPayload](docs/ReceiveP2MAdvicepostPayload.md)
 - [ReceiveP2MAdvicepostResponse](docs/ReceiveP2MAdvicepostResponse.md)
 - [ReceiveP2MpostPayload](docs/ReceiveP2MpostPayload.md)
 - [ReceiveP2MpostResponse](docs/ReceiveP2MpostResponse.md)



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