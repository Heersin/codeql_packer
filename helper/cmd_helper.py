import argparse

class CmdHelper:
    def create_default_parser(self):
        parser = argparse.ArgumentParser(description='Pack Codeql Command')
        parser.add_argument(
            '-l', '--language', 
            choices=['cpp', 'javascript'],
            required=True,
            help="choose language of target project")

        parser.add_argument(
            '-c', '--compile-cmd', 
            help='compile command for project, for {all} mode only')

        parser.add_argument(
            '-m', '--mode', 
            required=True, 
            choices=['scan-only','all'],
            help='scan-only, the path should be a codeql database, else a source code path')

        # path
        parser.add_argument('path', help='A codeql database or source path')
        return parser
    
    def create_parser_from_scratch():
        pass