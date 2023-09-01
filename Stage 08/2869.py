import math

A, B, V = map(int, input().split())
n = (V - A) / (A - B)

print(abs(math.ceil(n + 1)))
