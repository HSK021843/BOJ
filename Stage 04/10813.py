N, M = map(int, input().split()) # N: 바구니 개수, M: 바꾸는 횟수
lst = []

for a in range(N):
    lst.append(a + 1)

for i in range(M):
    i, j = map(int, input().split())
    lst[i - 1], lst[j - 1] = lst[j - 1], lst[i- 1]

for ele in lst:
    print(ele, end = ' ')
