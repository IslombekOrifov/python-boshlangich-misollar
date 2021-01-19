#Topshiriq! Nolga teng bo'lmagan ikkita son berilgan ularning yig'indisi, ko'paytmasi
#              va har birining moduli aniqlansin!

#Oddiy
a = 8
b = 8
y = a + b
k = a * b
d1 = abs(a)
d2 = abs(b)
print(f"{a} va {b} sonlarining yig'indisi {y} ga, \nko'paytmasi {k} ga, \nmodullari {d1} va {d2} ga teng!")

#Funksiya
def amallar():
    a = int(input("son kiriting: "))
    b = int(input("son kiriting: "))
    y = int(a) + int(b)
    k = int(a) * int(b)
    d1 = abs(int(a))
    d2 = abs(int(b))
    # modulni python funksiya abs bilan topilmaganda if shart operatori bilan yasaladi!
    # yani
    # if int(a)<0:
    #   d1 = int(a)*(-1)
    # else:
    #   d1 = int(a)
    print(f"{a} va {b} sonlarining yig'indisi {y} ga, \nko'paytmasi {k} ga, \nmodullari {d1} va {d2} ga teng!")

amallar()