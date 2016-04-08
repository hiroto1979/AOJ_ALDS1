def dictionary_command(command):
    if command[0] == "insert":
        dictionary.add(command[1])
    elif command[0] == "find":
        if command[1] in dictionary:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    n = int(input())
    
    dictionary = set()
    for i in range(n):
        command = input().split()
        dictionary_command(command)
