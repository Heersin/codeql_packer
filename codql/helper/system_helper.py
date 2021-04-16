import os

class SysHelper:
    def check_dir(self, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return False
            return True
        return False

    def create_file(self, path):
        print(os.getcwd())
        return os.mkdir(path)        