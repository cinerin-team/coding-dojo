#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
#hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

# Szám bekérése
szam = int(input("Kérem a számot: "))

oszt3al = szam % 3 == 0
oszt5el = szam % 5 == 0

if oszt3al and oszt5el:
    print ("a szam osztato 3-al es 5-el")
elif oszt3al:
    print("a szam osztato 3-al es 5-el nem")
elif oszt5el:
    print("a szam osztato 5-el es 3-al nem")
else:
    print ("a szam nem oszthato 5-el es 3-al sem")


