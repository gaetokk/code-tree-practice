n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
def go(x, y, cur_dir, cur_mov):
    if cur_dir == 'E':
        x = x + cur_mov
    elif cur_dir == 'S':
        y = y - cur_mov
    elif cur_dir == 'W':
        x = x - cur_mov
    elif cur_dir == 'N':
        y = y + cur_mov
    # print(x, y)
    return x, y

x, y = 0, 0
for i in range(n):
    cur_dir = dir[i]
    cur_mov = dist[i]
    x, y = go(x, y, cur_dir, cur_mov)

print(x, y)

