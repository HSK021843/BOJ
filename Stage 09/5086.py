state = True

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        state = False
        break

    if A % B == 0:
        print("multiple")
    else:
        if B % A == 0:
            print("factor")
        else:
            print("neither")
