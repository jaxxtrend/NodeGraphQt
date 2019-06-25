#!/usr/bin/python
# -*- coding: utf-8 -*-

from NodeGraphQt import credentials as crds
from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

description = (
    'Node graph framework that can be re-implemented into applications that '
    'supports PySide & PySide2'
)
classifiers = [
    'Programming Language :: Python :: 3.7.2',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
]

install_requirements = parse_requirements(
    'requirements.txt', session='session')
requirements = [str(requirement.req) for requirement in install_requirements]

setup(
    name=str(crds.__module_name__),
    version=str(crds.__version__),
    author=str(crds.__author__),
    author_email=str(crds.__email__),
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    url=str(crds.__url__),
    packages=find_packages(exclude=["example_nodes"]),
    classifiers=classifiers,
    include_package_data=True,
    python_requires=">=3.6"
)
