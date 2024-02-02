import sys

S = set()

for _ in range(int(input())):
    line = sys.stdin.readline().split()
    command = line[0]

    if command == 'add':
        S.add(int(line[1]))
    elif command == 'remove':
        S.discard(int(line[1]))
    elif command == 'check':
        if int(line[1]) in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        x = int(line[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif command == 'all':
        S = set(range(1, 21))
    elif command == 'empty':
        S.clear()
