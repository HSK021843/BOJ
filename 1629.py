def mult(x, y, z):
    if y == 1:
        return x % z
    else:
        tmp = mult(x, y // 2, z)
        if y % 2 == 0:
            return (tmp * tmp) % z
        else:
            return (tmp * tmp * x) % z

def calc(x, y, z):
    res = mult(x, y, z)
    return res
    

A, B, C = map(int, input().split())
answer = calc(A, B, C)

print(answer)
