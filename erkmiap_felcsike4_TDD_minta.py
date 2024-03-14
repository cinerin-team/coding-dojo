# Írj egy Python programot, amely bekér egy egész számot a felhasználótól
# és kiírja a képernyőre, hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

def oszthato_e_ottel_vagy_harommal(szam):
    if szam % 5 == 0 or szam % 3 == 0:
        return "igen osztható 5-tel vagy 3-mal"
    else:
        return "nem osztható 5-tel vagy 3-mal"


if __name__ == '__main__':
    jo = False

    while not jo:
        kerdes = input("mondj egy szamot: ")
        try:
            print(oszthato_e_ottel_vagy_harommal(int(kerdes)))
        except ValueError:
            print("mondom számot!!!!!")
        else:
            jo = True  # mert akkor megállhatunk
