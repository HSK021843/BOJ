ipt = input()
count = [0] * 26

for ele in ipt:
    code = ord(ele)

    if code > 90:
        count[code - 97] += 1
    else:
        count[code - 65] += 1

mx = max(count)
idx = count.index(max(count))
cnt = 0

for n in count:
    if  mx == n:
        cnt += 1
        if cnt >= 2:
            output = "?"
            break

    output = chr(idx + 65)
print(output)
