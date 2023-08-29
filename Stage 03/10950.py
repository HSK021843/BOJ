T = int(input())
lst = []

for i in range(T):
    A, B = map(int, input().split())
    lst.append(A + B)

for res in lst:
    print(res)
