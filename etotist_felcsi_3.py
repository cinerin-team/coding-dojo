#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és
#kiír egy érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

x = int (input("Kérem a pontszámot, köszönöm: "))

#if type(x) != int:
#    print("Hülye vagy!")
#    exit(1)

if x < 50:
    print("Az érdemjegye 1-es!")
elif x < 60:
    print("Az érdemjegye 2-es!")
elif x < 70:
    print("Az érdemjegye 3-as!")
elif x < 85:
    print("Az érdemjegye 4-es!")
elif x > 100:
    print ("Hülye vagy!")
else:
    print("Az érdemjegye 5-ös!")
