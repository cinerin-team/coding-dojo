#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és
#kiírja a képernyőre, hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

x = int (input("Kérem a számot, köszönöm: "))

if x % 3 == 0 or x % 5 == 0:
    print("Igen, osztható 3-mal vagy 5-tel!")
else:
    print("Nem, nem osztható 3-mal vagy 5-tel!")