while True:
    n = int(input())

    if n == -1:
        break
    
    lst = []

    for i in range(1, n):
        if n % i == 0:
            lst.append(i)


    if sum(lst) == n:
        print(f"{n} = ", end = ' ')
        if sum(lst) == n:
            print(f"{n} = {' + '.join(map(str, lst))}")
    else:
        print(f"{n} is NOT perfect.")
