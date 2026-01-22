N, K, P, T = map(int, input().split())
handshakes = []
for _ in range(T):
    t, x, y = map(int, input().split())
    handshakes.append((t, x, y))

# 시간 순으로 정렬
handshakes.sort()

# 감염 여부
infected = [False] * (N + 1)
infected[P] = True

# 감염자가 악수한 횟수 (감염자가 아니면 의미 없음)
shake_count = [0] * (N + 1)

for t, x, y in handshakes:
    # 악수 전 상태 저장 (중요!)
    x_was_infected = infected[x]
    y_was_infected = infected[y]
    x_can_spread = x_was_infected and shake_count[x] < K
    y_can_spread = y_was_infected and shake_count[y] < K
    
    # 전염 처리
    if x_can_spread:
        infected[y] = True
    if y_can_spread:
        infected[x] = True
    
    # 악수 횟수 증가 (감염자였던 경우만)
    if x_was_infected:
        shake_count[x] += 1
    if y_was_infected:
        shake_count[y] += 1

# 출력
for i in range(1, N + 1):
    print(1 if infected[i] else 0, end='')