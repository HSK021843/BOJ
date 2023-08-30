N = int(input())
lst = []

for i in range(N):
    lst.append(int(input()))

for _ in range(N):
    for i in range(N - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

for i in range(N):
    print(lst[i])
