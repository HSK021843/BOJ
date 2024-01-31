square = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
area = 0

for _ in range(n):
    x, y = map(int, input().split())
    x_1, y_1 = x + 10, y + 10

    for y_2 in range(y, y_1):
        for x_2 in range(x, x_1):
            if square[y_2][x_2] == 0:
                square[y_2][x_2] = 1
                area += 1

print(area)
