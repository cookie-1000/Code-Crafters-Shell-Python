import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        if command == "exit":
            sys.exit()
        else: 
            print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()
