cpp_config = [
    'query-lib/official/cpp/codeql-suites/cpp-security-and-quality.qls',
    'query-lib/official/cpp/codeql-suites/cpp-security-extended.qls',
]

js_config = []



# exported
lang_configs = {
    'cpp' : cpp_config,
    'javascript' : js_config
}

need_compile = ['cpp', 'java']