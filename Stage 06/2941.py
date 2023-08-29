HR_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
cnt = 0

for idx in range(len(word) - 1):
    if word[idx] + word[idx + 1] in HR_lst:
        cnt += 1
        idx += 2

for idx in range(len(word) - 2):
    if word[idx] + word[idx + 1] + word[idx + 2] in HR_lst:
        cnt += 1
        idx += 3

print(len(word) - cnt)
