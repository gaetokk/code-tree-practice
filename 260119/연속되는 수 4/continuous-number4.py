n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cur_num = 1
max_num = cur_num

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cur_num += 1
    else:
        cur_num = 1
    max_num = max(max_num, cur_num)

print(max_num)