n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
matrix = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    cnt = 0
    x, y = points[i]
    if matrix[x][y] == 0:
        matrix[x][y] = 1
    if x - 1 > 0 and matrix[x-1][y] == 1:
        cnt += 1
    if x + 1 <= n and matrix[x+1][y] == 1:
        cnt += 1
    if y + 1 <= n and matrix[x][y+1] == 1:
        cnt += 1
    if y - 1 > 0 and matrix[x][y-1] == 1:
        cnt += 1
    if cnt == 3:
        print(1)
    elif cnt != 3:
        print(0)