# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="OTRXMPPLogger",
    author='Mike Gogulski',
    author_email='mike@gogulski.com',
    maintainer='Mike Gogulski',
    maintainer_email='mike@gogulski.com',
    url='https://github.com/mikegogulski/python-otrxmpplogger',
    version='1.0.0',
    packages=['OTRXMPPLogger', ],
    install_requires=[
         'xmpppy',
         'python-potr',
         'otrxmppchannel',
    ],
    license='Unlicense',
    description='A Python XMPP logging handler',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
)
