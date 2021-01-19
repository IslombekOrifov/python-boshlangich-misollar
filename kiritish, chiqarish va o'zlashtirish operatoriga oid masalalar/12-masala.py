#Topshiriq! To'g'ri uchuburchakning katetlari a va b berilgan. Uning gipotenuzasi c va perimetri p aniqlansin

#Oddiy
a = 3
b = 4
c = ((a**2) + (b**2))**(1/2)
p = a + b + c
print(f"katetlari {a} va {b} bo'lgan uchuburchakning gipotenuzasi {c} ga, \nperimetri {p} ga teng!")

#Funksiya
def amallar():
    a = int(input("son kiriting: "))
    b = int(input("son kiriting: "))
    c = ((a ** 2) + (b ** 2)) ** (1 / 2)
    p = a + b + c
    print(f"katetlari {a} va {b} bo'lgan uchuburchakning gipotenuzasi {c} ga, \nperimetri {p} ga teng!")

amallar()
