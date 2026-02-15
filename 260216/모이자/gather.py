n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_dist = 1000000
for i in range(n):
    i_dist = 0
    for k in range(n):
        if k != i:
            i_dist += abs(k - i) * A[k]
    min_dist = min(min_dist, i_dist)


print(min_dist)