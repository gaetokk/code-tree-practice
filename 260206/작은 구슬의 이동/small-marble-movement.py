n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

x, y = r, c
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):  # check whether position is out of grid
        move_dir = 3 - move_dir # change direction
    else:
        x, y = nx, ny

print(x, y)