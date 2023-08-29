A, B, C = map(int, input().split())

if A != B and B != C and C != A:
    state = 1
    number = max(A, B, C)
elif A == B and B != C:
    state = 2
    number = A
elif A == C and B != A:
    state = 3
    number = A
elif B == C and A != B:
    state = 4
    number = B
else:
    state = 5
    number = A

if state == 1:
    p = number * 100
elif state >= 2 and state <= 4:
    p = 1000 + number * 100
else:
    p = 10000 + number * 1000


print(p)
