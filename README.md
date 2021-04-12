# codeql_packer
Scripts to pack codeql

## Dependencies
### Python Requirements
argparse

### Codeql binaries
[codeql-cli](https://github.com/github/codeql-cli-binaries)

### query-libs
find them in [codeql](https://github.com/github/codeql)
example : cpp related suites is set in codeql/cpp/

## Usage
```
usage: main.py [-h] -l {cpp,javascript} [-c COMPILE_CMD] -m {scan-only,all} path

Pack Codeql Command

positional arguments:
  path                  A codeql database or source path

optional arguments:
  -h, --help            show this help message and exit
  -l {cpp,javascript}, --language {cpp,javascript}
                        choose language of target project
  -c COMPILE_CMD, --compile-cmd COMPILE_CMD
                        compile command for project, for {all} mode only
  -m {scan-only,all}, --mode {scan-only,all}
                        scan-only, the path should be a codeql database, else a source
                        code path

```

### example
python main.py -l cpp -m all -c 'make' ~/blackhole/fuzz/socat
