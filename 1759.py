def valid_password(L, C, chars, last_char, vowel_cnt, consonant_cnt, password):
    global passwords
    vowels = "aeiou"

    if len(password) == L:
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            passwords.append(password)
        return

    if last_char >= C:
        return

    if chars[last_char] in vowels:
        valid_password(L, C, chars, last_char + 1, vowel_cnt + 1, consonant_cnt, password + chars[last_char])
    else:
        valid_password(L, C, chars, last_char + 1, vowel_cnt, consonant_cnt + 1, password + chars[last_char])

    valid_password(L, C, chars, last_char + 1, vowel_cnt, consonant_cnt, password)



L, C = map(int, input().split())
chars = sorted(list(input().split()))
passwords = []

valid_password(L, C, chars, 0, 0, 0, "")

for password in passwords:
    print(password)
