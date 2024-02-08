def removeBomb(word, bomb):
    stack = []
    bomb_len = len(bomb)
    
    for chr in word:
        stack.append(chr)
        
        if ''.join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()
                
    return ''.join(stack)


word = input()
bomb = input()

res = removeBomb(word, bomb)

if len(res) == 0:
    print("FRULA")
else:
    print(res)
