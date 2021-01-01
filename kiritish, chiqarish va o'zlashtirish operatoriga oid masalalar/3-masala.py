# Topshiriq!  To'g'ri to'rtburchakning tomonlari a va b berilgan. Uning yuzasi va perimetri aniqlansin!

# oddiy usul
a = 5
b = 4
s = a*b
p = 2*(a+b)
print(f"tomoni {a} va {b} bo'lgan to'g'ri to'rtburchakning yuzasi: {s} ga, perimetri: {p} ga teng")

#Funksiya
a = input("To'g'ri to'rtburchakning tomonini kiriting: ")
b = input("To'g'ri to'rtburchakning tomonini kiriting: ")
def tyuzper(c, d):
    s = int(c) * int(d)
    p = 2 * (int(c) + int(d))
    print(f"tomoni {c} va {d} bo'lgan to'g'ri to'rtburchakning yuzasi: {s} ga, perimetri: {p} ga teng")
tyuzper(a, b)