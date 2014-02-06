#!/usr/bin/env python
"""
logmein_app
===========

Connect remotely to a django project
"""

from setuptools import setup, find_packages

import logmein_app

setup(
    name="logmein_app",
    version=logmein_app.__version__,
    description="Connect remotely to a django project",
    long_description=__doc__,
    author=logmein_app.__author__,
    url="https://github.com/raphapassini/logmein",
    license=logmein_app.__license__,

    classifiers=[
        "Intended Audience :: Developers",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    platforms='any',

    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['logmein_app=logmein_app.main:main'],
    },
)

