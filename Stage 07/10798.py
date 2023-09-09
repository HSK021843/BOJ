import sys

wordlst = [sys.stdin.readline().strip() for _ in range(5)]
longest = 0

for word in wordlst:
    if len(word) > longest:
        longest = len(word)

for i in range(longest):
    for j in range(5):

        if i < len(wordlst[j]):
            sys.stdout.write(wordlst[j][i])

# 원본 코드에서 sys모듈로 input(), print() 대체
# 원본 코드

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
