wordlst = [input() for _ in range(5)]
longest = 0

for word in wordlst:
    if len(word) > longest:
        longest = len(word)

for i in range(longest):
    for j in range(5):

        try:
            print(wordlst[j][i], end = "")
        except IndexError:
            j += 1
