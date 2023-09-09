N, B = map(int, input().split())
numOrd = []

while N > 0:
    save = N % B

    if save >= 10:
        save = chr(save + 55)
        numOrd.append(save)
    else:
        numOrd.append(str(save))
    
    N //= B

for i in range(len(numOrd) - 1, -1, -1):
    print(numOrd[i], end="")
