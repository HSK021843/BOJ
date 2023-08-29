grade_lst = (('A+', 4.5), ('A0', 4.0), ('B+', 3.5), ('B0', 3.0), ('C+', 2.5),
         ('C0', 2.0), ('D+', 1.5), ('D0', 1.0), ('F', 0.0))
tot_score = 0
tot_credit = 0

for _ in range(20):
    info = input().split()
    credit = float(info[1])
    grade = info[2]

    for idx in range(len(grade_lst)):
        if grade == grade_lst[idx][0]:
            tot_score += (credit * grade_lst[idx][1])
            tot_credit += credit
        else:
            pass

avg_grade = tot_score / tot_credit
print(avg_grade)
