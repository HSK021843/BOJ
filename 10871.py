N, X = map(int, input().split())
A = list(map(int, input().split()))

for ele in A:
    if X > ele:
        print(ele, end = ' ')
