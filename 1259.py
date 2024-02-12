numbers = []

while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        numbers.append(n)

for number in numbers:
    str_num = str(number)
    if str_num == str_num[::-1]: 
        print('yes')
    else:
        print('no')
