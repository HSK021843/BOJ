mx = 0
idx = 0

for i in range(9):
    N = int(input())
    
    if mx < N:
        mx = N
        idx = (i + 1)
        
print(mx)
print(idx)
