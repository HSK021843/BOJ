def least_count(K, values):
    global count
    for value in reversed(values):
        if K >= value:
            count += K // value
            K %= value
            

N, K = map(int, input().split())
values = []
count = 0

for _ in range(N):
    values.append(int(input()))

least_count(K, values)
print(count)
