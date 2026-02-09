N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
cnt = 0
is_stop = 0

for i in range(N):
    if is_stop == 1:
        break
    dir_i = dir[i]
    dist_i = dist[i]

    for _ in range(dist_i):
        cnt += 1
        if dir_i == 'E':
            x, y = x + dx[0], y + dy[0]
        elif dir_i == 'S':
            x, y = x + dx[1], y + dy[1]
        elif dir_i == 'W':
            x, y = x + dx[2], y + dy[2]
        else:
            x, y = x + dx[3], y + dy[3]
        if x == 0 and y == 0:
            is_stop = 1
            print(cnt)
            break
            

if is_stop == 0:
    print(-1)
