import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
length = 0

for _ in range(N):
    order = sys.stdin.readline().split()
    command = order[0].strip()

    if command == "push":
        queue.append(int(order[1]))
        length += 1

    elif command == "pop":
        if queue:
            print(queue.popleft())
            length -= 1
        else:
            print(-1)

    elif command == "size":
        print(length)

    elif command == "empty":
        if length == 0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if length == 0:
            print(-1)
        else:
            print(queue[0])

    elif command == "back":
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
