N = int(input())
x_lst = []
y_lst = []

for _ in range(N):
    A, B = map(int, input().split())
    x_lst.append(A)
    y_lst.append(B)

x_length = max(x_lst) - min(x_lst)
y_length = max(y_lst) - min(y_lst)

print(x_length * y_length)
