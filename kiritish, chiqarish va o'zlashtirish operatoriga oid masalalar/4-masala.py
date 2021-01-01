# Topshiriq!  Aylananig diametri d berilgan. Uning uzunligi aniqlansin!

# oddiy usul
d = 3
p = 3.14
l = p*d
print(f"diametri {d} bo'lgan Aylananing uzunligi: {l} ga teng")

#Funksiya
a = input("Aylananing diametrini kiriting: ")
def auzunlik(c):
    l = p * int(c)
    print(f"diametri {c} bo'lgan Aylananing uzunligi: {l} ga teng")
auzunlik(a)