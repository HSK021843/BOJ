lst = [int(input()) for _ in range(3)]

if sum(lst) != 180:
    print("Error")
else:
    cnt = len(set(lst))

    if cnt == 1:
        print("Equilateral")
    elif cnt == 2:
        print("Isosceles")
    else:
        print("Scalene")
