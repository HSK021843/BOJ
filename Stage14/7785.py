n = int(input())
lst = []

for _ in range(n):
    name, log = map(str, input().split())

    if log == "enter":
        lst.append(name)
    elif log == "leave":
        lst.remove(name)

lst.sort(reverse = True)

for ele in lst:
    print(ele)
