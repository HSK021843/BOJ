import sys

A, B = map(int, input().split())
lst = []

target = 0
while A >= B:
    rest = A % B
    target = A // B

    if rest >= 10:
        ch = chr(rest + 55)
        lst.append(ch)
    else:
        lst.append(str(rest))

    A = target

if target >= 10:
    ch = chr(target + 55)
    lst.append(ch)
else:
    lst.append(str(target))


print(''.join(lst))
