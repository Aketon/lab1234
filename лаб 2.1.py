eng = int(input())
ger = int(input())
en_student = []
ge_student = []
for i in range(eng):
    en_student.append(input())
for j in range(ger):
    ge_student.append(input())
ambidext = set(en_student).intersection(set(ge_student))
if eng + ger - len(ambidext) * 2 == 0:
    print('NO')
else:
    print(eng + ger - len(ambidext) * 2)