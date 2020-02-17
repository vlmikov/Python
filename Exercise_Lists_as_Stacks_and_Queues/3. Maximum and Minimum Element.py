
result = []
n = int(input())

for i in range(n):
    command = input().split()
    if len(command) > 1:
        result.append(int(command[1]))

    if result:
        if command[0] == "2":
            result.pop()
        elif command[0] == "3":
            print(max(result))
        elif command[0] == "4":
            print(min(result))

ccc = len(result)
for i in range(len(result)):
    if i == ccc-1:
        print(result.pop())
    else:
        print(f"{result.pop()}, ", end="")
