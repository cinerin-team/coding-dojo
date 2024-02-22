#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és
#kiírja a képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

x = input("Kérem a számot, köszönöm: ")
try:
    szam = int(x)
    #print("Ez egy szám!")
except ValueError:
    raise Exception("Ez nem szám te kretén!")

result = ""
for i in range(3,szam,3):
    result += str(i) + ", "

#a string utolsó 2 karakterének törlése, egyébként lehetne len(result)-2
result = result[:-2]
print(result)
