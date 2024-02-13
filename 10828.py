import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    orders = sys.stdin.readline().split()
    order = orders[0]

    if order == "push":
        number = int(orders[1])
        stack.append(number)
        
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif order == "size":
        print(len(stack))
        
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
        
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
