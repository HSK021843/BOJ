N, M = map(int, input().split())
lst = [0] * N

for _ in range(M):
    A, B, C = map(int, input().split())
    for i in range(A - 1, B):
        lst[i] = C

print(lst)
