# -*- coding: utf-8 -*-
from setuptools import setup

import saml2idp

with open('README.rst') as readme:
    description = readme.read()


with open('HISTORY.rst') as history:
    changelog = history.read()


setup(
    name='dj-saml-idp',
    version=saml2idp.__version__,
    author='Sebastian Vetter',
    author_email='sebastian@mobify.com',
    description='SAML 2.0 IdP for Django',
    long_description='\n\n'.join([description, changelog]),
    install_requires=[
        'Django>=1.8',
        'pyopenssl>=0.16',
        'BeautifulSoup4>=4.4.0',
        'lxml',
        'structlog'],
    license='MIT',
    packages=['saml2idp'],
    url='http://github.com/mobify/dj-saml-idp',
    zip_safe=False,
    include_package_data=True,
)
