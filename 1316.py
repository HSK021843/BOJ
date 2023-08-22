N = int(input())
cnt = 0

for _ in range(N):
    visited = set()
    prev = None
    state = True
    
    word = input()
    for ele in word:
        if prev is None or prev == ele:
            prev = ele
        else:
            if ele in visited:
                state = False
                break
            visited.add(prev)
            prev = ele            

    if state is True:
        cnt += 1

print(cnt)
        
