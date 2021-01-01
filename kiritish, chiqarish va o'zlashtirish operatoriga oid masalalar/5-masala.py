# Topshiriq! Kubning yon tomoni a berilgan! Uning hajmini va to'la sirtini toping.

# Oddiy
a = 6
v = a**3
s = 6*(a**2)
print(f"Tomoni {a} bo'lgan kubning hajmi: {v} va to'la sirti {s} ga teng")

#Funksiya
a = input("Aylananing diametrini kiriting: ")
def hajmsirt(c):
    v = int(c) ** 3
    s = 6 * (int(c) ** 2)
    print(f"Tomoni {c} bo'lgan kubning hajmi: {v} va to'la sirti {s} ga teng")

hajmsirt(a)