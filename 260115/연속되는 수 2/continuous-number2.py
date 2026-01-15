n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt_max = 0
cur_max = 0

for i in range(n):
    if i == 0:
        cur_max = 1
    else:
        if arr[i] == arr[i-1]:
            cur_max += 1
            cnt_max = max(cnt_max, cur_max)
        else:
            cur_max = 1

cnt_max = max(cnt_max, cur_max)
print(cnt_max)

        