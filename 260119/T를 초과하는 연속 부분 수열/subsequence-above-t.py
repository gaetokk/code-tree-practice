n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
if arr[0] > t:
    cur_cnt = 1
else:
    cur_cnt = 0

max_cnt = cur_cnt

for i in range(1, n):
    if arr[i] > arr[i-1] and cur_cnt > 0:
        cur_cnt += 1            
    elif arr[i] > t:
        cur_cnt = 1
    else:
        cur_cnt = 0
    max_cnt = max(cur_cnt, max_cnt)


print(max_cnt)
