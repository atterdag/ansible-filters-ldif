#!/usr/bin/env python
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible-filters-ldif',
    version='0.0.2',
    description='Ansible filter to query or write LDIF.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Valdemar Lemche',
    author_email='valdmar@lemche.net',
    url='https://github.com/atterdag/ansible-filters-ldif',
    packages=[],
    license='GPLv3+',
    project_urls={
        'Bug Tracker': 'https://github.com/atterdag/ansible-filters-ldif/issues',
        'Documentation': 'https://github.com/atterdag/ansible-filters-ldif/blob/master/README.rst',
        'Source Code': 'https://github.com/atterdag/ansible-filters-ldif',
    },
    py_filters=[
        "ansible/plugins/filter/ldif",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    install_requires=[
        'ansible>=2.5.0',
        'python-ldap',
    ],
)
