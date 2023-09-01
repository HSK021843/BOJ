import sys

n = int(input())
lst = set()

for _ in range(n):
    name, log = sys.stdin.readline().split()

    if log == "enter":
        lst.add(name)
    else:
        lst.remove(name)


lst = sorted(lst, reverse = True)
print('\n'.join(lst))
