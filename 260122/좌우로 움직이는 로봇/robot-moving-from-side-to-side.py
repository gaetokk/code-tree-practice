n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

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
    for _ in range(t_b[i]):
        if d_b[i] == 'L':
            b_loc -= 1
        else:
            b_loc += 1
        b_dir.append(b_loc)


meet_cnt = 0
a_len = len(a_dir)
b_len = len(b_dir)

for i in range(1, min(a_len, b_len)):
    if a_dir[i] == b_dir[i]:
        if a_dir[i-1] != b_dir[i-1]:
            meet_cnt += 1

if b_len > a_len :
    for i in range(a_len, b_len):
        if b_dir[i] == a_dir[a_len-1]:
            if b_dir[i-1] != a_dir[a_len-1]:
                meet_cnt += 1

elif b_len < a_len :
    for i in range(b_len, a_len):
        if b_dir[b_len-1] == a_dir[i]:
            if b_dir[b_len-1] != a_dir[i-1]:
                meet_cnt += 1


print(meet_cnt)