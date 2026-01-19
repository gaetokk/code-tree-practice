N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
max_len = 1
cur_len = 1

for i in range(1, N):
    if arr[i] * arr[i-1] > 0:
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(cur_len, max_len)


print(max_len)
