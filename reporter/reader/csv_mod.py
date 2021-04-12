import csv
from .base_reader import BaseReader

'''
No header in the csv output, use index instead

0. Name
1. Query Description
2. Level ("example : error")
3. Message of Alert
4. Path of file
5. Start line
6. Start column
7. End line
8. End column
'''

class CsvReader(BaseReader):
    def __init__(self):
        self.files = []
        self.data = []

    def read(self, path):
        self.files.append(path)
        with open(path) as f:
            f_csv = csv.reader(f)
            
            for row in f_csv:
                row_data = {}
                row_data['name'] = row[0]
                row_data['level'] = row[2]
                row_data['message'] = row[3]
                row_data['path'] = row[4]

                pos_start = row[5] + ':' + row[6]
                pos_end = row[7] + ':' + row[8]
                pos = pos_start + ', ' + pos_end
                row_data['pos'] = pos

                self.data.append(row_data)

    def get_data(self):
        ret = {}
        ret['data'] = self.data
        ret['count'] = len(self.data)
        return ret