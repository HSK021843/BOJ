count = int(input())
lec = []

for _ in range(count):
    s, f = map(int, input().split())
    lec.append((f, s))

lec.sort()

lessons = 0
fin = 0

for i in range(count):
    if lec[i][1] >= fin:
        lessons += 1
        fin = lec[i][0]

print(lessons)
