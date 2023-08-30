T = int(input())

for _ in range(T):
    W, E = map(int, input().split())
    W_res = 1
    E_res = 1

    for i in range(E, E - W, -1):
        E_res *= i

    for j in range(W):
        W_res *= (j + 1)

    print(E_res // W_res)
