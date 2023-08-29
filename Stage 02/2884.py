T, M = map(int, input().split())
sub = 45

if M >= 45:
    print(f"{T} {M - sub}")
else: # M < 45
    M = 60 + (M - sub)
    if T > 0:
        print(f"{T - 1} {M}")
    else:
        print(f"23 {M}")
