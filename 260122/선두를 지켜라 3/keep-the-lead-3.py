N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
a_loc = 0
a_dir = []

for i in range(N):
    for _ in range(t[i]):
        a_loc += v[i]
        a_dir.append(a_loc)


b_loc = 0
b_dir = []

for i in range(M):
    for _ in range(t2[i]):
        b_loc += v2[i]
        b_dir.append(b_loc)


is_first = 0
is_change = 0

for i in range(len(a_dir)):
    if a_dir[i] > b_dir[i] and is_first != "A":
        is_change += 1
        is_first ="A"
    elif a_dir[i] < b_dir[i] and is_first != "B":
        is_change += 1
        is_first ="B"
    elif a_dir[i] == b_dir[i] and is_first != "AB":
        is_change += 1
        is_first ="AB"

print(is_change)
