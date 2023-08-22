N = int(input())

for i in range(N):
    spaces = " " * (N - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

for i in range(N - 2, -1, -1):
    spaces = " " * (N - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
