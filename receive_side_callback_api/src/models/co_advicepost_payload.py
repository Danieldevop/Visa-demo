# coding: utf-8

"""
    Receive Side Callback API

    To facilitate the implementation of mVisa, Visa provides mVisa Receive Side API specifications to clients who implement a set of outbound RESTful APIs (Receive Side APIs) so that Visa can call these APIs to request clients to process the transactions over the Internet.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CoAdvicepostPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, local_transaction_time=None, visa_transaction_id=None, originator_country_code=None, decimal_position_indicator=None, retrieval_reference_number=None, velocity_limit_indicator=None, agent_country_code=None, enc_consumer_name=None, message_type=None, rejection_code=None, local_transaction_date=None, enc_agent_pan=None, originator_bin=None, system_trace_audit_number=None, response_code=None, transaction_currency_code=None, enc_consumer_pan=None, agent_city=None, transaction_amount=None, auth_id_response=None, transmission_date_time=None):
        """
        CoAdvicepostPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'local_transaction_time': 'str',
            'visa_transaction_id': 'str',
            'originator_country_code': 'str',
            'decimal_position_indicator': 'str',
            'retrieval_reference_number': 'str',
            'velocity_limit_indicator': 'str',
            'agent_country_code': 'str',
            'enc_consumer_name': 'str',
            'message_type': 'str',
            'rejection_code': 'str',
            'local_transaction_date': 'str',
            'enc_agent_pan': 'str',
            'originator_bin': 'str',
            'system_trace_audit_number': 'str',
            'response_code': 'str',
            'transaction_currency_code': 'str',
            'enc_consumer_pan': 'str',
            'agent_city': 'str',
            'transaction_amount': 'str',
            'auth_id_response': 'str',
            'transmission_date_time': 'str'
        }

        self.attribute_map = {
            'local_transaction_time': 'localTransactionTime',
            'visa_transaction_id': 'visaTransactionId',
            'originator_country_code': 'originatorCountryCode',
            'decimal_position_indicator': 'decimalPositionIndicator',
            'retrieval_reference_number': 'retrievalReferenceNumber',
            'velocity_limit_indicator': 'velocityLimitIndicator',
            'agent_country_code': 'agentCountryCode',
            'enc_consumer_name': 'encConsumerName',
            'message_type': 'messageType',
            'rejection_code': 'rejectionCode',
            'local_transaction_date': 'localTransactionDate',
            'enc_agent_pan': 'encAgentPAN',
            'originator_bin': 'originatorBIN',
            'system_trace_audit_number': 'systemTraceAuditNumber',
            'response_code': 'responseCode',
            'transaction_currency_code': 'transactionCurrencyCode',
            'enc_consumer_pan': 'encConsumerPAN',
            'agent_city': 'agentCity',
            'transaction_amount': 'transactionAmount',
            'auth_id_response': 'authIdResponse',
            'transmission_date_time': 'transmissionDateTime'
        }

        self._local_transaction_time = local_transaction_time
        self._visa_transaction_id = visa_transaction_id
        self._originator_country_code = originator_country_code
        self._decimal_position_indicator = decimal_position_indicator
        self._retrieval_reference_number = retrieval_reference_number
        self._velocity_limit_indicator = velocity_limit_indicator
        self._agent_country_code = agent_country_code
        self._enc_consumer_name = enc_consumer_name
        self._message_type = message_type
        self._rejection_code = rejection_code
        self._local_transaction_date = local_transaction_date
        self._enc_agent_pan = enc_agent_pan
        self._originator_bin = originator_bin
        self._system_trace_audit_number = system_trace_audit_number
        self._response_code = response_code
        self._transaction_currency_code = transaction_currency_code
        self._enc_consumer_pan = enc_consumer_pan
        self._agent_city = agent_city
        self._transaction_amount = transaction_amount
        self._auth_id_response = auth_id_response
        self._transmission_date_time = transmission_date_time

    @property
    def local_transaction_time(self):
        """
        Gets the local_transaction_time of this CoAdvicepostPayload.
        The time the transaction takes place, expressed in the local time of the originator. The time is in hhmmss format.

        :return: The local_transaction_time of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._local_transaction_time

    @local_transaction_time.setter
    def local_transaction_time(self, local_transaction_time):
        """
        Sets the local_transaction_time of this CoAdvicepostPayload.
        The time the transaction takes place, expressed in the local time of the originator. The time is in hhmmss format.

        :param local_transaction_time: The local_transaction_time of this CoAdvicepostPayload.
        :type: str
        """
        if local_transaction_time is None:
            raise ValueError("Invalid value for `local_transaction_time`, must not be `None`")

        self._local_transaction_time = local_transaction_time

    @property
    def visa_transaction_id(self):
        """
        Gets the visa_transaction_id of this CoAdvicepostPayload.
        Numeric. It contains a right-justified, VisaNet generated Transaction Identifier (TID) that is unique for each request. The identifier links original messages to subsequent messages, such as those for exception item processing and clearing record.

        :return: The visa_transaction_id of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._visa_transaction_id

    @visa_transaction_id.setter
    def visa_transaction_id(self, visa_transaction_id):
        """
        Sets the visa_transaction_id of this CoAdvicepostPayload.
        Numeric. It contains a right-justified, VisaNet generated Transaction Identifier (TID) that is unique for each request. The identifier links original messages to subsequent messages, such as those for exception item processing and clearing record.

        :param visa_transaction_id: The visa_transaction_id of this CoAdvicepostPayload.
        :type: str
        """
        if visa_transaction_id is None:
            raise ValueError("Invalid value for `visa_transaction_id`, must not be `None`")

        self._visa_transaction_id = visa_transaction_id

    @property
    def originator_country_code(self):
        """
        Gets the originator_country_code of this CoAdvicepostPayload.
        A 3-digit ISO-4217 code that identifies the country of the originating BIN.<br>Refer to <a href=\"/request_response_codes#iso_country_codes\">ISO codes</a>.

        :return: The originator_country_code of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._originator_country_code

    @originator_country_code.setter
    def originator_country_code(self, originator_country_code):
        """
        Sets the originator_country_code of this CoAdvicepostPayload.
        A 3-digit ISO-4217 code that identifies the country of the originating BIN.<br>Refer to <a href=\"/request_response_codes#iso_country_codes\">ISO codes</a>.

        :param originator_country_code: The originator_country_code of this CoAdvicepostPayload.
        :type: str
        """
        if originator_country_code is None:
            raise ValueError("Invalid value for `originator_country_code`, must not be `None`")

        self._originator_country_code = originator_country_code

    @property
    def decimal_position_indicator(self):
        """
        Gets the decimal_position_indicator of this CoAdvicepostPayload.
        Indicates the number of decimal positions following the amount field. This field is to be sent as NULL if it is not populated.

        :return: The decimal_position_indicator of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._decimal_position_indicator

    @decimal_position_indicator.setter
    def decimal_position_indicator(self, decimal_position_indicator):
        """
        Sets the decimal_position_indicator of this CoAdvicepostPayload.
        Indicates the number of decimal positions following the amount field. This field is to be sent as NULL if it is not populated.

        :param decimal_position_indicator: The decimal_position_indicator of this CoAdvicepostPayload.
        :type: str
        """
        if decimal_position_indicator is None:
            raise ValueError("Invalid value for `decimal_position_indicator`, must not be `None`")

        self._decimal_position_indicator = decimal_position_indicator

    @property
    def retrieval_reference_number(self):
        """
        Gets the retrieval_reference_number of this CoAdvicepostPayload.
        Numeric. It is a key data element for matching a message to others within a given transaction set. The same number appears in all related messages: response, advice, reversal, chargeback, chargeback reversal, or representment. The format is recommended to be <b>ydddhhnnnnnn</b>.

        :return: The retrieval_reference_number of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._retrieval_reference_number

    @retrieval_reference_number.setter
    def retrieval_reference_number(self, retrieval_reference_number):
        """
        Sets the retrieval_reference_number of this CoAdvicepostPayload.
        Numeric. It is a key data element for matching a message to others within a given transaction set. The same number appears in all related messages: response, advice, reversal, chargeback, chargeback reversal, or representment. The format is recommended to be <b>ydddhhnnnnnn</b>.

        :param retrieval_reference_number: The retrieval_reference_number of this CoAdvicepostPayload.
        :type: str
        """
        if retrieval_reference_number is None:
            raise ValueError("Invalid value for `retrieval_reference_number`, must not be `None`")

        self._retrieval_reference_number = retrieval_reference_number

    @property
    def velocity_limit_indicator(self):
        """
        Gets the velocity_limit_indicator of this CoAdvicepostPayload.
        <b>Conditional</b>. This field contains the velocity limit related information that Acquirer can use in making the authorization decision:<ul><li>1 = 1-day count or amount exceeded.</li><li>2 = 7-day count or amount exceeded.</li><li>3 = 30-day count or amount exceeded.</li></ul>The field is populated with priority of 1, 2 and then 3.<br>This field is sent if recipient has opted for VisaNet to forward them the OCT when a velocity limit has been exceeded.<br>This field will be sent as NULL if it is not populated.

        :return: The velocity_limit_indicator of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._velocity_limit_indicator

    @velocity_limit_indicator.setter
    def velocity_limit_indicator(self, velocity_limit_indicator):
        """
        Sets the velocity_limit_indicator of this CoAdvicepostPayload.
        <b>Conditional</b>. This field contains the velocity limit related information that Acquirer can use in making the authorization decision:<ul><li>1 = 1-day count or amount exceeded.</li><li>2 = 7-day count or amount exceeded.</li><li>3 = 30-day count or amount exceeded.</li></ul>The field is populated with priority of 1, 2 and then 3.<br>This field is sent if recipient has opted for VisaNet to forward them the OCT when a velocity limit has been exceeded.<br>This field will be sent as NULL if it is not populated.

        :param velocity_limit_indicator: The velocity_limit_indicator of this CoAdvicepostPayload.
        :type: str
        """

        self._velocity_limit_indicator = velocity_limit_indicator

    @property
    def agent_country_code(self):
        """
        Gets the agent_country_code of this CoAdvicepostPayload.
        <b>Conditional</b>. Recipient may replace this field with 2-letter ISO 3166 country code of the agent, if different than the value provided by the originator. Visa settlement reports would contain the value provided by recipient. This field is to be sent as NULL if it is not populated.

        :return: The agent_country_code of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._agent_country_code

    @agent_country_code.setter
    def agent_country_code(self, agent_country_code):
        """
        Sets the agent_country_code of this CoAdvicepostPayload.
        <b>Conditional</b>. Recipient may replace this field with 2-letter ISO 3166 country code of the agent, if different than the value provided by the originator. Visa settlement reports would contain the value provided by recipient. This field is to be sent as NULL if it is not populated.

        :param agent_country_code: The agent_country_code of this CoAdvicepostPayload.
        :type: str
        """

        self._agent_country_code = agent_country_code

    @property
    def enc_consumer_name(self):
        """
        Gets the enc_consumer_name of this CoAdvicepostPayload.
        Consumer name. If consumer name is greater than 30 characters, then only first 30 characters will be expected. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data).

        :return: The enc_consumer_name of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._enc_consumer_name

    @enc_consumer_name.setter
    def enc_consumer_name(self, enc_consumer_name):
        """
        Sets the enc_consumer_name of this CoAdvicepostPayload.
        Consumer name. If consumer name is greater than 30 characters, then only first 30 characters will be expected. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data).

        :param enc_consumer_name: The enc_consumer_name of this CoAdvicepostPayload.
        :type: str
        """
        if enc_consumer_name is None:
            raise ValueError("Invalid value for `enc_consumer_name`, must not be `None`")

        self._enc_consumer_name = enc_consumer_name

    @property
    def message_type(self):
        """
        Gets the message_type of this CoAdvicepostPayload.
        Possible values based on Message Type Identifier are:<br><ul><li>0200 : 'Recipient Timeout'</li><li>0220 : 'Advice' (STIP decline advice)</li><li>0210 : 'Reject' (VIP reject)</li></ul>

        :return: The message_type of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this CoAdvicepostPayload.
        Possible values based on Message Type Identifier are:<br><ul><li>0200 : 'Recipient Timeout'</li><li>0220 : 'Advice' (STIP decline advice)</li><li>0210 : 'Reject' (VIP reject)</li></ul>

        :param message_type: The message_type of this CoAdvicepostPayload.
        :type: str
        """
        if message_type is None:
            raise ValueError("Invalid value for `message_type`, must not be `None`")

        self._message_type = message_type

    @property
    def rejection_code(self):
        """
        Gets the rejection_code of this CoAdvicepostPayload.
        Only populated if Advice message type is ‘Reject’. This field contains the VisaNet rejection code.

        :return: The rejection_code of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._rejection_code

    @rejection_code.setter
    def rejection_code(self, rejection_code):
        """
        Sets the rejection_code of this CoAdvicepostPayload.
        Only populated if Advice message type is ‘Reject’. This field contains the VisaNet rejection code.

        :param rejection_code: The rejection_code of this CoAdvicepostPayload.
        :type: str
        """
        if rejection_code is None:
            raise ValueError("Invalid value for `rejection_code`, must not be `None`")

        self._rejection_code = rejection_code

    @property
    def local_transaction_date(self):
        """
        Gets the local_transaction_date of this CoAdvicepostPayload.
        It contains the local month and day on which the transaction was originated. The date is in mmdd format.

        :return: The local_transaction_date of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._local_transaction_date

    @local_transaction_date.setter
    def local_transaction_date(self, local_transaction_date):
        """
        Sets the local_transaction_date of this CoAdvicepostPayload.
        It contains the local month and day on which the transaction was originated. The date is in mmdd format.

        :param local_transaction_date: The local_transaction_date of this CoAdvicepostPayload.
        :type: str
        """
        if local_transaction_date is None:
            raise ValueError("Invalid value for `local_transaction_date`, must not be `None`")

        self._local_transaction_date = local_transaction_date

    @property
    def enc_agent_pan(self):
        """
        Gets the enc_agent_pan of this CoAdvicepostPayload.
        Agent PAN. 16-digit PAN as created from the mVisa agent ID captured by the consumer from agent information display option. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption.

        :return: The enc_agent_pan of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._enc_agent_pan

    @enc_agent_pan.setter
    def enc_agent_pan(self, enc_agent_pan):
        """
        Sets the enc_agent_pan of this CoAdvicepostPayload.
        Agent PAN. 16-digit PAN as created from the mVisa agent ID captured by the consumer from agent information display option. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption.

        :param enc_agent_pan: The enc_agent_pan of this CoAdvicepostPayload.
        :type: str
        """
        if enc_agent_pan is None:
            raise ValueError("Invalid value for `enc_agent_pan`, must not be `None`")

        self._enc_agent_pan = enc_agent_pan

    @property
    def originator_bin(self):
        """
        Gets the originator_bin of this CoAdvicepostPayload.
        This BIN number identifies the originator of Cash-Out payment transaction.

        :return: The originator_bin of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._originator_bin

    @originator_bin.setter
    def originator_bin(self, originator_bin):
        """
        Sets the originator_bin of this CoAdvicepostPayload.
        This BIN number identifies the originator of Cash-Out payment transaction.

        :param originator_bin: The originator_bin of this CoAdvicepostPayload.
        :type: str
        """
        if originator_bin is None:
            raise ValueError("Invalid value for `originator_bin`, must not be `None`")

        self._originator_bin = originator_bin

    @property
    def system_trace_audit_number(self):
        """
        Gets the system_trace_audit_number of this CoAdvicepostPayload.
        Numeric. It is a key data element used to match a response to its request or to match a message to others for a given transaction.

        :return: The system_trace_audit_number of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._system_trace_audit_number

    @system_trace_audit_number.setter
    def system_trace_audit_number(self, system_trace_audit_number):
        """
        Sets the system_trace_audit_number of this CoAdvicepostPayload.
        Numeric. It is a key data element used to match a response to its request or to match a message to others for a given transaction.

        :param system_trace_audit_number: The system_trace_audit_number of this CoAdvicepostPayload.
        :type: str
        """
        if system_trace_audit_number is None:
            raise ValueError("Invalid value for `system_trace_audit_number`, must not be `None`")

        self._system_trace_audit_number = system_trace_audit_number

    @property
    def response_code(self):
        """
        Gets the response_code of this CoAdvicepostPayload.
        Contains a code (also known as 'Action Code') that defines the response to a request. Refer to actionCode

        :return: The response_code of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this CoAdvicepostPayload.
        Contains a code (also known as 'Action Code') that defines the response to a request. Refer to actionCode

        :param response_code: The response_code of this CoAdvicepostPayload.
        :type: str
        """
        if response_code is None:
            raise ValueError("Invalid value for `response_code`, must not be `None`")

        self._response_code = response_code

    @property
    def transaction_currency_code(self):
        """
        Gets the transaction_currency_code of this CoAdvicepostPayload.
        The 3-digit ISO-4217 code in this field reflects the currency associated to the transactionAmount field.

        :return: The transaction_currency_code of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._transaction_currency_code

    @transaction_currency_code.setter
    def transaction_currency_code(self, transaction_currency_code):
        """
        Sets the transaction_currency_code of this CoAdvicepostPayload.
        The 3-digit ISO-4217 code in this field reflects the currency associated to the transactionAmount field.

        :param transaction_currency_code: The transaction_currency_code of this CoAdvicepostPayload.
        :type: str
        """
        if transaction_currency_code is None:
            raise ValueError("Invalid value for `transaction_currency_code`, must not be `None`")

        self._transaction_currency_code = transaction_currency_code

    @property
    def enc_consumer_pan(self):
        """
        Gets the enc_consumer_pan of this CoAdvicepostPayload.
        Consumer PAN. This is a 16-digit PAN. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption.

        :return: The enc_consumer_pan of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._enc_consumer_pan

    @enc_consumer_pan.setter
    def enc_consumer_pan(self, enc_consumer_pan):
        """
        Sets the enc_consumer_pan of this CoAdvicepostPayload.
        Consumer PAN. This is a 16-digit PAN. The field is sent in encrypted format using the AES GCM (i.e. Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM)) algorithm for JSON Web Encryption (JWE) objects with 256-bit key (i.e. the shared secret between Visa and client for encryption and decryption of payload data). The field data type will be string(16-19) after decryption.

        :param enc_consumer_pan: The enc_consumer_pan of this CoAdvicepostPayload.
        :type: str
        """

        self._enc_consumer_pan = enc_consumer_pan

    @property
    def agent_city(self):
        """
        Gets the agent_city of this CoAdvicepostPayload.
        Agent city name.

        :return: The agent_city of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._agent_city

    @agent_city.setter
    def agent_city(self, agent_city):
        """
        Sets the agent_city of this CoAdvicepostPayload.
        Agent city name.

        :param agent_city: The agent_city of this CoAdvicepostPayload.
        :type: str
        """
        if agent_city is None:
            raise ValueError("Invalid value for `agent_city`, must not be `None`")

        self._agent_city = agent_city

    @property
    def transaction_amount(self):
        """
        Gets the transaction_amount of this CoAdvicepostPayload.
        Transaction amount in agent on currency. In case the agent currency is not the same as the consumer currency, then originator will perform currency conversion before submitting the transaction.

        :return: The transaction_amount of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """
        Sets the transaction_amount of this CoAdvicepostPayload.
        Transaction amount in agent on currency. In case the agent currency is not the same as the consumer currency, then originator will perform currency conversion before submitting the transaction.

        :param transaction_amount: The transaction_amount of this CoAdvicepostPayload.
        :type: str
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")

        self._transaction_amount = transaction_amount

    @property
    def auth_id_response(self):
        """
        Gets the auth_id_response of this CoAdvicepostPayload.
        Contains the authorization code provided by the recipient when a transaction is approved. Visa recommends that recipient maintains uniqueness of this code for a given merchant PAN, however Visa would not maintain any checks for uniqueness. This field is to be sent as NULL if it is not populated.

        :return: The auth_id_response of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._auth_id_response

    @auth_id_response.setter
    def auth_id_response(self, auth_id_response):
        """
        Sets the auth_id_response of this CoAdvicepostPayload.
        Contains the authorization code provided by the recipient when a transaction is approved. Visa recommends that recipient maintains uniqueness of this code for a given merchant PAN, however Visa would not maintain any checks for uniqueness. This field is to be sent as NULL if it is not populated.

        :param auth_id_response: The auth_id_response of this CoAdvicepostPayload.
        :type: str
        """

        self._auth_id_response = auth_id_response

    @property
    def transmission_date_time(self):
        """
        Gets the transmission_date_time of this CoAdvicepostPayload.
        The date and time the request was submitted to Visa. Format: MMDDhhmmss.

        :return: The transmission_date_time of this CoAdvicepostPayload.
        :rtype: str
        """
        return self._transmission_date_time

    @transmission_date_time.setter
    def transmission_date_time(self, transmission_date_time):
        """
        Sets the transmission_date_time of this CoAdvicepostPayload.
        The date and time the request was submitted to Visa. Format: MMDDhhmmss.

        :param transmission_date_time: The transmission_date_time of this CoAdvicepostPayload.
        :type: str
        """
        if transmission_date_time is None:
            raise ValueError("Invalid value for `transmission_date_time`, must not be `None`")

        self._transmission_date_time = transmission_date_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CoAdvicepostPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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