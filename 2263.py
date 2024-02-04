import sys
sys.setrecursionlimit(10**6)

def make_preorder(inord_L, inord_R, postord_L, postord_R):
    global inorder, postorder
    if inord_L > inord_R or postord_L > postord_R:
        return
    
    root = postorder[postord_R]
    print(root, end = ' ')
    
    left = inorder_index[root] - inord_L
    make_preorder(inord_L, inord_L + left - 1, postord_L, postord_L + left - 1)
    
    right = inord_R - inorder_index[root]
    make_preorder(inord_R - right + 1, inord_R, postord_R - right, postord_R - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_index = [0] * (n + 1)

for i in range(n):
    inorder_index[inorder[i]] = i
    
make_preorder(0, n - 1, 0, n - 1)
