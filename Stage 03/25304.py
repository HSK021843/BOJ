X = int(input())
N = int(input())
tot = 0

for i  in range(N):
    a, b = map(int, input().split())
    tot += (a * b)

if tot == X:
    print("Yes")
else:
    print("No")
