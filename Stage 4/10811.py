lst = []
N, M = map(int, input().split())
for i in range(N):
    lst.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    lst_N = lst[i - 1:j]
    lst_N.reverse()

    lst[i - 1:j] = lst_N
    
for ele in lst:
    print(ele, end = ' ')




# 5 4 -> 1 2 3 4 5
# 1 2 -> 2 1 3 4 5
# 3 4 -> 2 1 4 3 5
# 1 4 -> 3 4 1 2 5
# 2 2 -> 3 4 1 2 5
