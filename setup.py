#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup

setup(
    name='twitterbot',
    version='0.1.0',
    author='thricedotted',
    author_email='thricedotted@gmail.com',
    packages=['twitterbot'],
    description='A simple Python framework for creating Twitter bots.',
    install_requires=[
        "tweepy >= 2.3"
    ],
)
