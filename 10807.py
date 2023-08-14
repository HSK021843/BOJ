N = int(input())
lst = list(input())
v = input()
cnt = 0

for i in lst:
    if i == v:
        cnt += 1

print(cnt)
