N, M = map(int, input().split())
S = set()
cnt = 0

for _ in range(N):
    string = input()
    S.add(string)

for _ in range(M):
    check = input()
    
    if check in S:
        cnt += 1


print(cnt)
