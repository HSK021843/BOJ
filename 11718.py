while True:
    try:
        word = input()

        if word == '':
            break
        else:
            print(word)
            
    except EOFError:
        break
