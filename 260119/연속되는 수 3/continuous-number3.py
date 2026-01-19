N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
max_len = 0
cur_len = 0

if arr[0] > 0:
    is_pos = True
    cur_len = 1
else:
    is_pos = False

for i in range(1, N):
    if arr[i] * arr[i-1] > 0:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 1


print(max_len)