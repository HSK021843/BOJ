N = int(input())
res = 1

if N == 0:
    res = 1

else:
    for i in range(N):
        res *= (i + 1)

print(res)
    
