import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        if command == "exit":
            sys.exit()
        elif command[:4]=="echo":
            print (command[5:])
        elif command[:4]=="type":
            if command[5:] in ["echo","exit","type"]:
                print (command[5:]+ " is a shell builtin")
            else:
                print (f"{command[5:]}: not found")
                continue
        else: 
            print(f"{command}: command not found")
    
        
if __name__ == "__main__":
    main()
