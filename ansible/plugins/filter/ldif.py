'''(c) 2019, @atterdag
   You should have received a copy of the GNU General Public License
   along with module. If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.module_utils.six.moves import StringIO
from ldif import LDIFWriter, LDIFRecordList


class FilterModule(object):
    ''' Ansible LDIF filter class
    '''

    def filters(self):
        ''' Method to map filter names in Ansible to methods in class
        '''
        return {
            'from_ldif': self.from_ldif,
            'to_ldif': self.to_ldif
        }

    @classmethod
    def encode_values(cls, entry_payload):
        ''' Encode all entries of all lists in dictionary to bytes.
        '''
        encoded_dict = {}
        for key, list in entry_payload.items():
            encoded_list = []
            for entry in list:
                encoded_list.append(entry.encode('utf-8'))
                encoded_dict[key] = encoded_list
        return encoded_dict

    @classmethod
    def from_ldif(cls, data):
        ''' Convert LDIF data to dictionary
        '''
        try:
            ldif_record_list = LDIFRecordList(StringIO(data))
            ldif_record_list.parse()
            return ldif_record_list.all_records
        except Exception:
            raise AnsibleFilterError(
                'Invalid LDIF data for LDIFRecordList (%s)' % data)

    @classmethod
    def to_ldif(cls, data):
        ''' Convert list of dictionary to LDIF. See
            https://github.com/atterdag/ansible-filters-ldif for how to
            format dictionary.
        '''
        if isinstance(data, list):
            try:
                ldif_data = StringIO()
                ldif_writer = LDIFWriter(ldif_data)
                for entry in data:
                    ldif_writer.unparse(str(entry[0]), dict(entry[1]))
                return ldif_data.getvalue()
            except Exception:
                raise AnsibleFilterError(
                    'Invalid input data for to_ldif filter (%s)' % data)
        else:
            raise AnsibleFilterError(
                'Input data to_ldif filter is not a list(%s)' % data)
