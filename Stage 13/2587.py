numlst = []

for _ in range(5):
    n = int(input())
    numlst.append(n)

numlst.sort()
avg = sum(numlst) / 5

print(int(avg))
print(numlst[2])
