import sys

def sugar_bag(N):
    bag = sys.maxsize
    for five in range(N // 5 + 1):
        for three in range(N // 3 + 1):
            total = five * 5 + three * 3

            if total == N:
                bag = min(bag, five + three)

    if bag == sys.maxsize:
        return -1

    return bag


N = int(input())
res = sugar_bag(N)
print(res)
