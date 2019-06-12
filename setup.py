#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools

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

setuptools.setup(
    name='NodeGraphQt',
    version='0.0.5',
    author='Johnny Chan',
    author_email='johnny@chantasticvfx.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jchanvfx/NodeGraphQt',
    packages=setuptools.find_packages(exclude=["example_nodes"]),
    classifiers=classifiers,
    include_package_data=True,
)


"""
python setup.py sdist
sudo python setup.py install
"""