#!/usr/bin/env python
"""Python Module setup script."""
"""Ref: https://docs.python.org/3/distutils/setupscript.html."""
import setuptools  # noqa: E402

with open("README.rst", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='ansible-filters-ldif',
    version='0.0.10',
    description='Ansible filter to read or write LDIF.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    author='Valdemar Lemche',
    author_email='valdmar@lemche.net',
    url='https://github.com/atterdag/ansible-filters-ldif',
    packages=[],
    license='GPLv3+',
    project_urls={
        'Bug Tracker': 'https://github.com/atterdag/ansible-filters-ldif/issues',  # noqa: E501
        'Documentation': 'https://github.com/atterdag/ansible-filters-ldif/blob/master/README.rst',  # noqa: E501
        'Source Code': 'https://github.com/atterdag/ansible-filters-ldif',  # noqa: E501
    },
    py_modules=[
        "ansible/plugins/filter/ldif",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa: E501
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    install_requires=[
        'ansible>=2.5.0',
        'python-ldap',
    ],
)
