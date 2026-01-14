x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
checked = [[0] * 2000 for _ in range(2000)]

for x in range(x1[0]+1000, x2[0]+1000):
    for y in range(y1[0]+1000, y2[0]+1000):
        checked[x][y] = 1

for x in range(x1[1]+1000, x2[1]+1000):
    for y in range(y1[1]+1000, y2[1]+1000):
        if checked[x][y] == 1:
            checked[x][y] = 0
        else:
            continue

min_x = 2000
min_y = 2000
max_x = 0
max_y = 0
found =  False

for x in range(0, 2000):
    for y in range(0, 2000):
        if checked[x][y] == 1:
            found = True
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

if found == False:
    print(0)
else:
    print((max_x - min_x + 1)*(max_y - min_y + 1))