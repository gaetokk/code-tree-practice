n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
checked = [[0] * 200 for _ in range(200)]
square = 0

for i in range(n):
    for x_p in range(x[i]+100, x[i]+108):
        for y_p in range(y[i]+100, y[i]+108):
            if checked[x_p][y_p] == 0:
                checked[x_p][y_p] = 1
                square += 1
            else:
                continue


print(square)