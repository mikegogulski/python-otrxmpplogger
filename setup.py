# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="OTRXMPPLogger",
    author='Mike Gogulski',
    author_email='mike@gogulski.com',
    maintainer='Mike Gogulski',
    maintainer_email='mike@gogulski.com',
    url='https://github.com/mikegogulski/python-otrxmpplogger',
    version='1.0.1',
    packages=['otrxmpplogger', ],
    install_requires=[
        'xmpppy',
        'python-potr',
        'otrxmppchannel',
    ],
    license='Unlicense',
    description='Logging with OTR (Off-the-Record Messaging) and XMPP',
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
