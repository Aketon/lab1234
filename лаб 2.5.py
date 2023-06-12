number_chyot = int(input())
number_Tribonachi = [1,1,1]
a = []
for i in range(number_chyot):
    if i < 3:
        a.append(number_Tribonachi[i])
    if i > 2:
        a.append(a[i-1] + a[i-2] + a[i-3])
print(a)



