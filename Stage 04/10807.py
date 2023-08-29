N = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0

for ele in lst:
    if ele == v:
        cnt += 1

print(cnt)
