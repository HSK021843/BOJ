state = True
while state:
    lst = list(map(int, input().split()))
    sorted(lst)

    if sum(lst) == 0:
        state = False
        break
    
    elif lst[0] + lst[1] <= lst[2]:
        print("Invalid")
        
    else:
        cnt = len(set(lst))
        if cnt == 1:
            print("Equilateral")
        elif cnt == 2:
            print("Isosceles")
        else:
            print("Scalene")
