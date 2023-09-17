def quarter(N):
    count = N // 25
    rest = N - 25 * count
    
    return rest, count


def dime(N):
    count = N // 10
    rest = N - 10 * count
    
    return rest, count


def nickel(N):
    count = N // 5
    rest = N - 5 * count
    
    return rest, count


def penny(N):
    count = N // 1
    rest = N - 1 * count
    
    return rest, count


N = int(input())

for _ in range(N):
    change = int(input())

    rest, quarter_count = quarter(change)
    rest, dime_count = dime(rest)
    rest, nickel_count = nickel(rest)
    rest, penny_count = penny(rest)

    print(f"{quarter_count} {dime_count} {nickel_count} {penny_count}")
