lst = []

for _ in range(10):
    ipt = int(input())
    rst = ipt % 42
    lst.append(rst)

lst = set(lst) # 집합은 중복을 허용하지 않으므로
same_cnt = 10 - len(lst) # 리스트의 길이(10)에서 집합의 원소 개수를 빼면 겹치는 숫자 개수가 나온다
print(10 - same_cnt) # 이렇게 구한 중복 개수를 10에서 빼면 서로 다른 숫자의 개수가 나온
