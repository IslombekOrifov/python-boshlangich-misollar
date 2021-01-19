#Topshiriq! Nolga teng bo'lmagan ikkita son berilgan ularning yig'indisi, ko'paytmasi
#              va har birining kvadrati aniqlansin!

#Oddiy
a = 8
b = 8
y = a + b
k = a * b
d1 = a**2
d2 = b ** 2
print(f"{a} va {b} sonlarining yig'indisi {y} ga, \nko'paytmasi {k} ga, \nkvadratlari {d1} va {d2} ga teng!")

#Funksiya
def amallar():
    a = int(input("son kiriting: "))
    b = int(input("son kiriting: "))
    y = int(a) + int(b)
    k = int(a) * int(b)
    d1 = int(a) ** 2
    d2 = int(b) ** 2
    print(f"{a} va {b} sonlarining yig'indisi {y} ga, \nko'paytmasi {k} ga, \nkvadratlari {d1} va {d2} ga teng!")

amallar()
