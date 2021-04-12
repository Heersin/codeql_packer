from helper.cmd_helper import CmdHelper
from helper.system_helper import SysHelper
from codeql.codeql import run_codeql

def init_workspace():
    sys_op = SysHelper()

    if not sys_op.check_dir('databases/'):
        sys_op.create_file('databases/')
    
    if not sys_op.check_dir('output/'):
        sys_op.create_file('output/')
    

def main():
    cmd_parser = CmdHelper()
    sys_op = SysHelper()

    parser = cmd_parser.create_default_parser()
    args = parser.parse_args()

    init_workspace()

    run_codeql(args)

    print('[*]Finish')


if __name__ == '__main__':
    main()
