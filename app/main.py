import os
import sys
import subprocess

built_ins = {"echo", "exit", "type"}

def find_executable(cmd: str):
    dirs = os.getenv("PATH", "").split(os.pathsep)
    for d in dirs:
        path = os.path.join(d, cmd)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        line = input()

        if line.strip() == "":
            continue

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "exit":
            return

        elif cmd == "echo":
            if line.startswith("echo "):
                print(line[5:])
            else:
                print()

        elif cmd == "type":
            if len(args) == 0:
                print("type: missing argument")
                continue

            target = args[0]
            if target in built_ins:
                print(f"{target} is a shell builtin")
            else:
                path = find_executable(target)
                if path is not None:
                    print(f"{target} is {path}")
                else:
                    print(f"{target}: not found")

        else:
            path = find_executable(cmd)
            if path is None:
                print(f"{cmd}: command not found")
            else:
                subprocess.run([cmd, *args], executable=path)

if __name__ == "__main__":
    main()
