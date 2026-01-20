n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
a_dir = []
a_loc = 0

for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'L':
            a_loc -= 1
        else:
            a_loc += 1
        a_dir.append(a_loc)


b_dir = []
b_loc = 0
for i in range(m):
    for _ in range(t2[i]):
        if d2[i] == 'L':
            b_loc -= 1
        else:
            b_loc += 1
        b_dir.append(b_loc)


is_meet = False
is_meet_index = -1

for a, b in zip(a_dir, b_dir):
    is_meet_index += 1
    if a == b:
        print(is_meet_index + 1)
        is_meet = True
        break

if is_meet == False:
    print(-1)