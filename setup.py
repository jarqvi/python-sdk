# coding: utf-8

"""
    Liara

    Manage your services using our API 
    
    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "jarqvi-openapi-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "aenum",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Liara",
    author="OpenAPI Generator community",
    author_email="info@liara.ir",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Liara"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["paas.test", "dbaas.test", "dns.test", "mail.test", "object_storage.test"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Manage your services using our API 
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
    setup_requires=['wheel']
)
