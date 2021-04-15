import requests
from .base_reader import BaseReader

'''
Used for fetching data from restful API server
default : 127.0.0.1/5000
'''
class RestfulReader(BaseReader):
    def __init__(self):
        self.url = "http://127.0.0.1"
        self.port = 5000
        self.run_api = '/v1/runs'
        self.task_api = '/v1/tasks'

        self.run_ids = []
        self.data = []

    def get_run_by_rid(self, run_id):
        req_url = self.url + ':' + str(self.port) + self.run_api + '/' + str(run_id)
        response = requests.get(req_url)
        response = response.json()
        return response

    def get_tasks_by_rid(self, run_id):
        req_url = self.url + ':' + str(self.port) + self.task_api + '/' + str(run_id)
        response = requests.get(req_url)
        response = response.json()
        return response

    def read(self, run_id):
        self.run_ids.append(run_id)

        #run_meta = self.get_run_by_rid(run_id)
        tasks = self.get_tasks_by_rid(run_id)['data']
        for task in tasks:
            one_record = {}
            one_record['name'] = task['rule']
            one_record['path'] = task['filename']
            one_record['level'] = task['level']
            one_record['message'] = task['message']
            one_record['pos'] = task['pos']
            self.data.append(one_record)

    def get_data(self):
        ret = {}
        ret['data'] = self.data
        ret['count'] = len(self.data)
        return ret

if __name__ == '__main__':
    r = RestfulReader()
    r.read('2')
    recs = r.get_data()
    print(recs)
