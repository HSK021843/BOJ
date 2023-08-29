word = input()
lst = (('ABC', 2), ('DEF', 3), ('GHI', 4), ('JKL', 5), ('MNO', 6), ('PQRS', 7), ('TUV', 8), ('WXYZ', 9))
time = 0

for ele in word:
    for i in range(len(lst)):
        if ele in lst[i][0]:
            time += (lst[i][1] + 1)

print(time)
