import argparse
import generator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, help='project name')
    parser.add_argument(
        '-s', '--sarif', 
        action='append', 
        help='read sarif format file, can set multiple times')
    parser.add_argument(
        '-j', '--json',
        help='read from remote json server'
    )
    parser.add_argument(
        '-c', '--csv',
        action='append',
        help='read csv format file, can set multiple times')
    
    args = parser.parse_args()
    generator.generate(args)