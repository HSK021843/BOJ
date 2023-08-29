def radix_change(N):
    try:
        int(to_decimal_target)
    except ValueError:
        ch = ord(to_decimal_target) - 55
    else:
        ch = int(A[idx])

    return ch


A, B = map(str, input().split())
decimal = 0

for idx in range(len(A)):
    to_decimal_target = A[idx]
    
    number = radix_change(to_decimal_target)
    decimal += (number * (int(B) ** (len(A) - idx - 1)))

print(decimal)
