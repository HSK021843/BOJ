N, M = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for i in range(N * 2):
    ipt = list(map(int, input().split()))
    
    for j in range(M):
        lst[i % N][j] += ipt[j]


for i in range(N):
    for j in range(M):
        print(lst[i][j], end = ' ')
    print()
