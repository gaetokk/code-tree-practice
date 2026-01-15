n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
checked = [[0] * 200 for _ in range(200)]

color = "blue"

for i in range(n):
    if color == "blue":
        color = "red"
    else:
        color = "blue"
    
    for x in range(x1[i]+100, x2[i]+100):
        for y in range(y1[i]+100, y2[i]+100):
            checked[x][y] = color


cnt_blue = 0

for x in range(0, 200):
    for y in range(0, 200):
        if checked[x][y] == "blue":
            cnt_blue += 1

print(cnt_blue)