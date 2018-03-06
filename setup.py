#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='interview',
    version='0.1.1',
    description='Some sample code for use in interviews.',
    url="https://github.com/RueLaLa/python-interview",
    author='Rue La La',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'test': [
            'flake8',
            'mock',
            'pytest',
            'pytest-sugar',
        ]
    }
)
