#. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
#érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

x = int (input ("kerem a szamot: "))

#if type(x) != int:
#    print("hulye vagy bazdmeg")
#    exit(1)

if x <50:
    print("1-es")

elif x < 60:
    print("2-es")
elif x < 70:
    print("3-es")
elif x < 85:
    print("4-es")
elif x > 100:
    print("hulye vagy bazdmeg")
else:
    print("5-os")

