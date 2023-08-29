T = int(input())

for _ in range(T):
    ipt = input()
    A = int(ipt.split(' ')[0])
    B = ipt.split(' ')[1]

    for idx in range(len(B)):
        print(B[idx] * A, end = '')

    print()
