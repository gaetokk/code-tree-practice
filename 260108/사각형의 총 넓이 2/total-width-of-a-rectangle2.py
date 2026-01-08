n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

field = [[0] * 200]*200
ans = 0

for i in range(n):
    for a, b, c, d in zip(x1, y1, x2, y2):
        for x in range(a+100, c+100):
            for y in range(b+100, d+100):
                cur_point = field[x][y]
                if cur_point == 0:
                    cur_point = 1
                    ans += 1
                else:
                    continue

print(ans)