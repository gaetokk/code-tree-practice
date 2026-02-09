commands = input()

# Please write your code here.

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3
cnt = 0
is_stop = 0

for cmd in commands:
    if is_stop == 1:
        break
    cnt += 1
    if cmd == 'F':
        if dir_num == 0:
            x, y = x + dx[0], y + dy[0]
        elif dir_num == 1:
            x, y = x + dx[1], y + dy[1]
        elif dir_num == 2:
            x, y = x + dx[2], y + dy[2]
        else:
            x, y = x + dx[3], y + dy[3]
    elif cmd == 'L':
        dir_num = (dir_num - 1) % 4
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    if x == 0 and y == 0:
        is_stop = 1
        print(cnt)

if is_stop == 0:
    print(-1)