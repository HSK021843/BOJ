N = int(input())
lastnum = 0

i = 666
runtime = 0
while True:
    number = str(i)
    to_count = "666"

    if to_count in number:
        lastnum = i
        runtime += 1

    if runtime == N:
        break
    
    i += 1


print(lastnum)
