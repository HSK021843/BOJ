def fact(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fact(N - 1)

ipt = int(input())
res = fact(ipt)

print(res)
