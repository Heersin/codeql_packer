from .config import lang_configs, need_compile
import os

def get_db_name_from_path(path):
    return path.split('/')[-1]

class Task:
    def __init__(self, lang, mode, path, compile_cmd):
        self.language = lang
        self.suites = lang_configs[lang]

        if lang in need_compile:
            self.compile = True
            self.compile_cmd = compile_cmd
        else:
            self.compile = False
        
        if mode == 'all':
            self.create_db = True
            self.src_path = path
            self.db_name = get_db_name_from_path(path)
            self.db_path = 'databases/' + self.db_name
        else:
            self.create_db = False
            self.db_path = path
            self.db_name = get_db_name_from_path(path)

        # set output name
        self.result_path_prefix = 'output/' + '{}_result'.format(self.db_name)
        
        # TODO more formats
        self.format = 'csv'
        self.result_path = self.result_path_prefix + '.' + self.format

    def create_codeql_db(self):
        if self.compile:
            cmd = 'codeql database create {} --language={} --source-root {} --command {}'.format(
                self.db_path,
                self.language,
                self.src_path,
                self.compile_cmd
            )
        else:
            cmd = 'codeql database create {} --language={} --source-root {}'.format(
                self.db_path,
                self.language,
                self.src_path
            )
        os.system(cmd)

    def run_analyze(self):
        count = 0
        for suite in self.suites:
            cmd = 'codeql database analyze {} {} --output={}_{} --format={}'.format(
                self.db_path, 
                suite, 
                self.result_path_prefix, 
                count, 
                self.format
            )
            count += 1
            os.system(cmd)
