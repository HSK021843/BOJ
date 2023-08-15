lst = [0] * 30 # [0, 0, 0 ... 0] 으로 0이 30개

for _ in range(28):
    idx = int(input())
    lst[idx - 1] = 1

for i in range(30):
    if lst[i] == 0:
        print(i + 1)
