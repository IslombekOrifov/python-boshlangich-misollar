#Topshiriq! Ikkita manfiy bo'lmagan son a va b berilgan! ularning o'rta geometrigi aniqlansin!

#Oddiy
a = 8
b = 8
s = (a*b)**(1/2)
print(f"{a} va  {b} sonlarining o'rta geometrigi: {s} ga teng!")

#Funksiya
a = int(input("son kiriting: "))
b = int(input("son kiriting: "))
def geometrik(c,d):
    s = (c + d) / 2
    print(f"{c} va  {d} sonlarining o'rta geometrigi: {s} ga teng!")
geometrik(a,b)