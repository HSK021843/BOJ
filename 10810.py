N, M = map(int, input().split())
lst = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        lst[i] = C

for idx in range(1, len(lst)):
    print(lst[idx], end = ' ')
