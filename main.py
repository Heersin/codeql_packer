from helper.cmd_helper import CmdHelper

def main():
    cmd_parser = CmdHelper()
    parser = cmd_parser.create_default_parser()
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
