import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        if command == "exit":
            sys.exit()
        if command[:4]=="echo":
            print (command[5:])
        else: 
            print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()
