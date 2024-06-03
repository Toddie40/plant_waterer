import subprocess

cmd = ["flask", "--app", "__init__:create_app('test')", "--debug", "run"]

subprocess.run(cmd)