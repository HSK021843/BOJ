import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for ele in sorted(lst):
    sys.stdout.write(f"{str(ele)}\n")
