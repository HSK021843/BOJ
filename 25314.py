N = int(input())
long_cnt = N // 4

for i in range(long_cnt):
    print("long", end = ' ')

    if long_cnt - 1 == i:
        print("int")
