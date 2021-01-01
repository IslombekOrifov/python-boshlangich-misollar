# Topshiriq! Paralelipipedning tomonlari a, b, c berilgan! Uning hajmini va to'la sirtini toping.

# Oddiy
a = 6
b = 5
c = 8
v = a*b*c
s = 2*(a*b + b*c + a*c)
print(f"Tomonlari { a, b, c } bo'lgan Paralelipipedning hajmi: {v} va to'la sirti {s} ga teng")

#Funksiya
a = input("Paralelipipedning tomonini kiriting: ")
b = input("Paralelipipedning tomonini kiriting: ")
c = input("Paralelipipedning tomonini kiriting: ")
def hajmsirt(d,e,f):
    v = int(d) * int(e) * int(f)
    s = 2 * (int(d) * int(e) + int(e) * int(f) + int(d) * int(f))
    print(f"Tomoni {d,e,f} bo'lgan Paralelipipedning hajmi: {v} va to'la sirti {s} ga teng")

hajmsirt(a, b, c)