from .task import Task

def run_codeql(args):
    print(args)
    lang = args.language
    mode = args.mode
    path = args.path
    compile_cmd = args.compile_cmd

    task = Task(lang, mode, path, compile_cmd)

    if task.create_db:
        task.create_codeql_db()

    task.run_analyze()