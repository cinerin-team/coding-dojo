# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
# képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege!

A = input("Kérem az A számot, köszönöm: ")

try:
    szam1 = int(A)
    if szam1 > 0:
        pass
    else:
        raise Exception("Te majom, pozitív egész szám kell te gyökér!")
except ValueError:
    raise Exception("Ez nem szám te kretén!")

# result = 0
# for i in range(szam1+1):
result = szam1
for i in range(szam1):
    result += i

print("Eredmény: " + str(result))