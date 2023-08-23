import sys

lst = []

for i in range(9):
    inner_lst = list(map(int, input().split()))
    lst.append(inner_lst)

mx = -sys.maxsize
x = 0
y = 0

for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] > mx:
            mx = lst[i][j]
            x = i
            y = j

print(mx)
print(f"{x + 1} {y + 1}")
