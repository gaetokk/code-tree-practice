N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
is_sick = [0] * (N + 1)
is_sick_2 = [0] * (N + 1)
is_sick_2[P] = 1

hs_cnt = [0] * 1000

for i in range(T):
    t, x, y = handshakes[i]
    hs_cnt[t] = (x, y)

for tm in hs_cnt:
    if tm != 0:
        x, y = tm
        if is_sick_2[x] > 0 and is_sick[x] < K:
            is_sick[x] += 1
            is_sick[y] += 1
            is_sick_2[y] = 1
        elif is_sick_2[y] > 0 and is_sick[y] < K:
            is_sick[x] += 1
            is_sick_2[x] = 1
            is_sick[y] += 1


for i in range(1, N+1):
    if is_sick[i] > 0:
        print(1, end='')
    else:
        print(0, end='')