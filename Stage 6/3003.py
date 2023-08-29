pieces = [1, 1, 2, 2, 2, 8] # 킹, 퀸, 룩, 비숍, 나잍, 폰 순서
r = input().split()

for i in range(6):
    pieces[i] -= int(r[i])
    print(pieces[i], end = ' ')
