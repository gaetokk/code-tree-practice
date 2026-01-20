n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a_dir = []
a_loc = 0
for i in range(n):
    for _ in range(t[i]):
        a_loc += v[i]
        a_dir.append(a_loc)

b_dir = []
b_loc = 0
for i in range(m):
    for _ in range(t2[i]):
        b_loc += v2[i]
        b_dir.append(b_loc)


cnt = 0
first = 0

for i in range(0, len(a_dir)):
    if a_dir[i] > b_dir[i]:
        if first == 'b' or first == 0:
            first = 'a'
            cnt += 1
    elif a_dir[i] < b_dir[i]:
        if first == 'a' or first == 0:
            first = 'b'
            cnt += 1

print(cnt-1)