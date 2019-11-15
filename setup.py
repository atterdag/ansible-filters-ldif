#!/usr/bin/env python
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible-filters-ldif',
    version='0.0.1',
    description='Ansible filter to query or write LDIF.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Valdemar Lemche',
    author_email='valdmar@lemche.net',
    url='https://github.com/atterdag/ansible-filters-ldif',
    packages=[],
    py_filters=[
        "ansible/plugins/filter/ldif",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'ansible>=2.5.0',
        'python-ldap',
    ],
)
