import sys
sys.setrecursionlimit(10**6)

def postorder(order):
    if len(order) == 0:
        return
    
    p = order[0]
    left = []
    right = []
    for i in range(1, len(order)):
        if order[i] < p:
            left.append(order[i])
        else:
            right.append(order[i])

    postorder(left)
    postorder(right)
    print(p)


preorder = []
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break
    
postorder(preorder)
