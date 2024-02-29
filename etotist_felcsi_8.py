# Írj egy Python programot, amely bekér egy valós (A) és egy egész (K) számot
# a felhasználótól és kiírja a képernyőre az AK hatvány értékét anélkül, hogy használnád a ** operátort!

A = input("Kérem az A számot, köszönöm: ")
K = input("Kérem a K számot, köszönöm: ")

try:
    szam1 = int(A)
    szam2 = int(K)
    # print("Ez egy szám!")
except ValueError:
    raise Exception("Ez nem szám te kretén!")

result = 1
# _-vel nem foglal le memóriát
for _ in range(szam2):
    result *= szam1

print("Az eredmény: " + str(result))
