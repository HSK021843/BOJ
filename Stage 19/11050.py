N, K = map(int, input().split())
N_res = 1
K_res = 1

for i in range(N, N - K, -1):
    N_res *= i

for j in range(K):
    K_res *= (j + 1)

print(int(N_res / K_res))
