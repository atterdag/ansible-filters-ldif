Ansible LDIF filter
===================

Ansible filter for querying, and writing LDIF.

.. image:: https://img.shields.io/pypi/v/ansible-filters-ldif.svg
   :alt: Latest version
   :target: https://pypi.python.org/pypi/ansible-filters-ldif/
.. image:: https://travis-ci.org/atterdag/ansible-filters-ldif.svg?branch=master
   :alt: Travis CI
   :target: https://travis-ci.org/atterdag/ansible-filters-ldif
.. image:: https://img.shields.io/badge/License-GPLv3-yellow.svg
   :alt: License: GPLv3
   :target: https://opensource.org/licenses/GPL-3.0

Install this Ansible Filter:

* via ``pip``:

::

  pip install ansible-filters-ldif

* via ``ansible-galaxy``:

::

  ansible-galaxy install 'git+https://github.com/atterdag/ansible-filters-ldif.git'

..


Ansible filters always runs on localhost.


Examples
--------

Convert dictionary to LDIF

.. code:: yaml

    ---
    - name: Create dictionary with entries
      set_fact:
        dictionary:
          - - dc=example,dc=com
            - dc:
                - example
              description:
                - This is a line longer than 79 characters, so LDIF breaks it up over multiple lines
              o:
                - example.com
              objectClass:
                - dcObject
                - organization
          - - ou=people,dc=example,dc=com
            - objectClass:
                - organizationalUnit
              ou:
                - people
          - - cn=Jane Doe,ou=people,dc=example,dc=com
            - cn:
                - Jane Doe
              mail:
                - jane.doe@example.com
              objectClass:
                - inetOrgPerson
              sn:
                - Doe
          - - cn=John Doe,ou=people,dc=example,dc=com
            - cn:
                - John Doe
              mail:
                - john.doe@example.com
              objectClass:
                - inetOrgPerson
              sn:
                - Doe
          - - ou=groups,dc=example,dc=com
            - objectClass:
                - organizationalUnit
              ou:
                - groups
          - - cn=users,ou=groups,dc=example,dc=com
            - cn:
                - users
              member:
                - cn=Jane Doe,ou=people,dc=example,dc=com
                - cn=John Doe,ou=people,dc=example,dc=com
              objectClass:
                - groupOfNames

    - name: "Convert dictionary to LDIF while writing it to /tmp/test.ldif using 'to_ldif' filter"
      copy:
        content: "{{ dictionary | to_ldif }}"
        dest: "/tmp/test.ldif"

Convert LDIF to JSON

.. code:: yaml

    ---
    - name: "Create multi-line string variable with LDIF data"
      set_fact:
        ldif: |
          dn: dc=example,dc=com
          dc: example
          description: This is one line which is longer than
           79 characters, so LDIF breaks it up over multiple lines
          objectClass: dcObject
          objectClass: organization
          o: example.com

          dn: ou=people,dc=example,dc=com
          objectClass: organizationalUnit
          ou: people

          dn: cn=Jane Doe,ou=people,dc=example,dc=com
          objectClass: inetOrgPerson
          cn: Jane Doe
          sn: Doe
          mail: jane.doe@example.com

          dn: cn=John Doe,ou=people,dc=example,dc=com
          objectClass: inetOrgPerson
          cn: John Doe
          sn: Doe
          mail: john.doe@example.com

          dn: ou=groups,dc=example,dc=com
          objectClass: organizationalUnit
          ou: groups

          dn: cn=users,ou=groups,dc=example,dc=com
          objectClass: groupOfNames
          cn: users
          member: cn=Jane Doe,ou=people,dc=example,dc=com
          member: cn=John Doe,ou=people,dc=example,dc=com

    - name: "Convert string to JSON whiĺe writing it to /tmp/test.json using 'from_ldif' filter"
      copy:
        content: "{{ (ldif | from_ldif) | to_nice_json }}"
        dest: "/tmp/test.json"


License
-------

`GPLv3 <https://opensource.org/licenses/GPL-3.0>`_.
