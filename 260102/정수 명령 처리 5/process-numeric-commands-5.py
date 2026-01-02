N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
arr = []
for cmd, n in zip(command, num):
    if cmd == "push_back":
        arr.append(n)
    elif cmd == "pop_back":
        arr = arr[:-1]
    elif cmd == "size":
        print(len(arr))
    elif cmd == "get":
        print(arr[n-1])
