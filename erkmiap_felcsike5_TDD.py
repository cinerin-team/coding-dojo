# Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

def ket_szam_osszege_a_haramdik(a, b, c):
    return (a + b == c) or (b + c == a) or (a + c == b)


if __name__ == '__main__':
    jo = False

    while not jo:
        kerdes = input("mondj egy szamot: ")
        kerdes2 = input("mondj mégegy szamot: ")
        kerdes3 = input("mondj és egy újabbat szamot: ")
        try:
            value = ket_szam_osszege_a_haramdik(int(kerdes), int(kerdes2), int(kerdes3))
            if value:
                print("egyenlő")
            else:
                print("nem egyenlő")
        except ValueError:
            print("mondom számot!!!!!")
        else:
            jo = True  # mert akkor megállhatunk
