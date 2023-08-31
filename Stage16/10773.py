K = int(input())
lst = []

for _ in range(K):
    ipt = int(input())

    if ipt == 0:
        lst.remove(lst[-1])
    else:
        lst.append(ipt)

sum_of_num = sum(lst)
print(sum_of_num)
