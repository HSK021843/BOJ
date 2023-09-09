def is_ENTER(situation):
    global namecnt, nameset
    
    namecnt += len(nameset)
    nameset = set()


N = int(input())
nameset = set()
namecnt = 0

for _ in range(N):
    situation = input()

    if situation == "ENTER":
        is_ENTER(situation)
    else:
        nameset.add(situation)

namecnt += len(nameset)

print(namecnt)
