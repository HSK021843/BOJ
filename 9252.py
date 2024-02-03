def Length(X, Y):
    n, m = len(X), len(Y)
    len_table = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                len_table[i][j] = len_table[i-1][j-1] + 1
            else:
                len_table[i][j] = max(len_table[i-1][j], len_table[i][j-1])
    
    return len_table

def LCS(X, Y, len_table):
    n, m = len(X), len(Y)
    lcs = []

    while n > 0 and m > 0:
        if X[n-1] == Y[m-1]:
            lcs.append(X[n-1])
            n, m = n-1, m-1
        elif len_table[n-1][m] > len_table[n][m-1]:
            n -= 1
        else:
            m -= 1

    return ''.join(reversed(lcs))


x = input()
y = input()

len_table = Length(x, y)
lcs = LCS(x, y, len_table)
lcs_length = len_table[len(x)][len(y)]

print(lcs_length)

if lcs_length != 0:
    print(lcs)

