from .base_reader import BaseReader
import json

class SarifReader(BaseReader):
    def __init__(self):
        self.files = []
        self.data = []

    def read(self, path):
        self.files.append(path)
        with open(path) as f:
            sarif_data = json.load(f)
            sarif_entries = sarif_data['runs'][0]['results']
            rules_table = sarif_data['runs'][0]['tool']['driver']['rules']

            for entry in sarif_entries:
                entry_data = {}
                entry_data['name'] = entry['ruleId']
                entry_data['message'] = entry['message']['text']
                
                # set path of vuln file
                postion_data = entry['locations'][0]['physicalLocation']
                entry_data['path'] = postion_data['artifactLocation']['uri']

                # set position of vuln 
                pos_start = str(postion_data['region']['startLine']) + ':' + str(postion_data['region']['startColumn'])
                if 'endLine' in postion_data['region']:
                    pos_end = str(postion_data['region']['endLine']) + ':' + str(postion_data['region']['endColumn'])
                else:
                    pos_end = str(postion_data['region']['startLine']) + ':' + str(postion_data['region']['endColumn'])
                entry_data['pos'] = pos_start + ', ' + pos_end

                # set level of this vuln
                rule_index = entry['ruleIndex']
                default_config = rules_table[rule_index]['defaultConfiguration']
                if 'level' in default_config:
                    entry_data['level'] = default_config['level']
                else:
                    entry_data['level'] = 'warning'

                print(entry_data)

                self.data.append(entry_data)

    def get_data(self):
        ret = {}
        ret['data'] = self.data
        ret['count'] = len(self.data)
        return ret