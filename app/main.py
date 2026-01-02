import os
import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            exit()
        elif command.startswith("echo"):
            command = command.split("echo ", 1)[1]
            print(command)
        elif command.startswith("type"):
            command = command.split("type ", 1)[1]
            if command in ["echo", "exit", "type"]:
                print(f"{command} is a shell builtin")
            else:
                dirs = os.getenv("PATH", "").split(os.pathsep)
                found = False
                for dir in dirs:
                    path = os.path.join(dir, command)
                    if os.path.isfile(path) and os.access(path, os.X_OK):
                        print(f"{command} is {path}")
                        found = True
                        break
                if not found:
                    print(f"{command}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()