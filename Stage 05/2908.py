def prt(lst):
    for ele in lst:
        print(ele, end = '')


A, B = map(list, input().split())

A.reverse()
B.reverse()

for i in range(3):
    if A[i] > B[i]:
        prt(A)
        break
    
    elif A[i] < B[i]:
        prt(B)
        break
