def answer(lans):
    start = 1
    end = max(lans)
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        
        for i in lans:
            count += i // mid
            
        if count >= K:
            start = mid + 1
        else:
            end = mid - 1

    return end


N, K = map(int, input().split())
lans = []

for _ in range(N):
    lan = int(input())
    lans.append(lan)
    
res = answer(lans)
print(res)
