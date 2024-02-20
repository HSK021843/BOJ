T = int(input())

for _ in range(T):
    N = int(input())
    univ_name = ""
    max_bottles = 0
    
    for _ in range(N):
        name, bottles = map(str, input().split())
        bottles = int(bottles)

        if bottles > max_bottles:
            univ_name = name
            max_bottles = bottles

    print(univ_name)
