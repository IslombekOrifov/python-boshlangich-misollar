# Topshiriq!  Doirning radiusi r berilgan. Uning uzunligi va yuzasi aniqlansin!

# oddiy usul
r = 3
p = 3.14
l = 2*p*r
s = p*(r**2)
print(f"radiusi {r} bo'lgan Aylananing uzunligi: {l} va yuzasi: {s} ga teng")

#Funksiya
a = input("Doiraning radiusini kiriting: ")
def doira(c):
    p = 3.14
    l = 2 * p * int(c)
    s = p * (int(c) ** 2)
    print(f"radiusi {c} bo'lgan Aylananing uzunligi: {l} va yuzasi: {s} ga teng")


doira(a)