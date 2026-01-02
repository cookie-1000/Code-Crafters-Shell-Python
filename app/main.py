import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        print(f"{command}: command not found")
        if command == "exit":
            sys.exit()
if __name__ == "__main__":
    main()
