def calculate(numbers):
    tg = numbers[0]
    
    for i in range(1, len(numbers)):
        tg -= numbers[i]
    
    return tg
    
def set(eq):    
    nums_sep_by_minus = eq.split('-')
    
    for idx in range(len(nums_sep_by_minus)):
        nums_sep_by_minus[idx] = sum(map(int, nums_sep_by_minus[idx].split('+')))
        
    result = calculate(nums_sep_by_minus)
    
    return result


eq = input()
nums_sep_by_minus = []
answer = set(eq)

print(answer)
