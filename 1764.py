N, M = map(int, input().split())

N_list = set()
M_list = set()

for i in range(N + M):
    name = input()
    
    if i + 1 <= N:
        N_list.add(name)
    else:
        M_list.add(name)

NnM = sorted(N_list.intersection(M_list))

print(len(NnM))

for NnM_name in NnM:
    print(NnM_name)
