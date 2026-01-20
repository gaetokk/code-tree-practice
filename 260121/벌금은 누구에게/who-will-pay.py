N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
score = [0] * (N + 1)
is_exist = 0

for i in range(M):
    stu = student[i]
    score[stu] += 1
    if score[stu] >= K:
        print(stu)
        is_exist = 1
        break

if is_exist == 0:
    print(-1)
