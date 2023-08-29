def avg(lst):
    sc_sum = 0
    
    for sc in lst:
         sc_sum += sc

    average = sc_sum / len(lst)
    return average


N = int(input())
lst = list(map(int, input().split()))
M = max(lst)

for idx in range(len(lst)):
    sc = lst[idx]
    lst[idx] = (sc / M * 100)


res = avg(lst)
print(res)
