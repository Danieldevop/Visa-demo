# coding: utf-8

"""
    Watch List Screening API

    The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual's name, city, and country input fields match against entries on the OFAC SDN lists.  The Watch List Screening API also provides an OFAC status value which represents how VisaNet would process the individual's information if used in a cross-border OCT transaction.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "src"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Watch List Screening API",
    author_email="",
    url="",
    keywords=["Swagger", "Watch List Screening API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Watch List Screening API provides an OFAC score value used for evaluation on how closely an individual&#39;s name, city, and country input fields match against entries on the OFAC SDN lists.  The Watch List Screening API also provides an OFAC status value which represents how VisaNet would process the individual&#39;s information if used in a cross-border OCT transaction.
    """
)
