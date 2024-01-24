def v10(ssdo, ssposle, chislo):
    chislo = str(chislo)[::-1]
    resalt = 0
    for i in range(len(chislo)):
        a = chislo[i]
        if ssdo == 16:
            a = a.replace("A", "10")
            a = a.replace("B", "11")
            a = a.replace("C", "12")
            a = a.replace("D", "13")
            a = a.replace("E", "14")
            a = a.replace("F", "15")
        resalt = resalt + int(a) * (ssdo ** i)
    return resalt
def is10(ssdo, ssposle, chislo):
    resalt = ""
    spisok = ['A', 'B', 'C', 'D', 'E', 'F']
    while chislo >= ssposle:
        a = chislo % ssposle
        if a > 9:
            a = spisok[int(str(a)[1])]
        resalt = resalt + str(a)
        chislo = chislo // ssposle
    if chislo > 9:
        chislo = str(chislo)[1]
        chislo = spisok[int(chislo)]
    resalt = resalt + str(chislo)
    resalt = resalt[::-1]
    return resalt
ssdo = int(input("Введите первоночальную систему счисления (2,3,8,10,16): "))
ssposle = int(input("Введите систему счисления, в которую надо перевести (2,3,8,10,16): "))
chislo = input("Введите число: ")
if ssdo != 10:
    chislo = v10(ssdo, ssposle, chislo)
resalt = is10(10, ssposle, int(chislo))
print(resalt)