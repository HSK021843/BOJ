def find(word, lst):
    for i in range(len(word)):
        tg = ord(word[i]) - 97
        
        if lst[tg] == -1:
            lst[tg] = i

    return lst


def print_res(lst):
    for ele in lst:
        print(ele, end = ' ')


S = input()
lst = [-1] * 26

find(S, lst)
print_res(lst)

