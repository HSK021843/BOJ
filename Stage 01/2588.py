A = int(input())
B = input()

third = A * int(B[2])
fourth = A * int(B[1])
fifth = A * int(B[0])
result = third + fourth * 10 + fifth * 100

print(third)
print(fourth)
print(fifth)
print(result)
