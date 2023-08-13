while True:
    A, B = map(int, input().split())

    if A <= 0 or A >= 10 or B <= 0 or B >= 10:
        break
    
    print(A + B)
