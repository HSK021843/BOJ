from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    order_input = list(sys.stdin.readline().split())
    order = order_input[0]

    if order == "push":
        number = order_input[1]
        queue.append(number)
        
    elif order == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif order == "size":
        print(len(queue))

    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
