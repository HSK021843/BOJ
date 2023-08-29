ipt = input()
half_point = (len(ipt) - 1) // 2
state = 1

if len(ipt) == 1:
    pass

else:
    if len(ipt) % 2 == 0:
        front = ipt[ : half_point + 1]
        end = ipt[half_point + 1 : ]
        end_rev = end[ : : -1]
    else:
        front = ipt[ : half_point]
        end = ipt[half_point + 1 : ]
        end_rev = end[ : : -1]
    
    for idx in range(len(front)):
        if front[idx] != end_rev[idx]:
            state = 0
            break
        else:
            state = 1

print(state)
