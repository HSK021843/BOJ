T, M = map(int, input().split())
time = int(input())

Tplus = time // 60
Mplus = time % 60
T += Tplus
M += Mplus

if M >= 60:
    T += 1
    M -= 60
    print(f"{T} {M}")
else:
    print(f"{T} {M}")
