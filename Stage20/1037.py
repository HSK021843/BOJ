total_count = int(input())
lst = list(map(int, input().split()))

if len(lst) == 1:
    print(lst[0] ** 2)
else:
    lst.sort()
    print(lst[0] * lst[-1])

