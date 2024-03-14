x = input("mondj egy számot\n")
try:
    a = int(x)
    print("sikeres konverzio")
except (ValueError, KeyError):
    # több tipusú exceptionra is rá lehet próbálni. de ha mást akarunk csinálni akkor mehet alá másik except
    raise Exception("ez egy string")
except :
    pass
    # lehet úgy is hogy bármit el akarunk kapni. nyilván ez itt nem történik meg mert már elkaptuk
else:
    print("ha nem volt hiba akkor ez is lesz")
finally:
    print("egyébként")
    # ez akkor is kiirodik ha volt hiba és akkor is ha nem de ha volt hiba akkor meg is áll a futás
    # ez pl akkor jó ha megnyitunk egy file-t és try-ban írunk bele, de finally-ban be lehet zárni

try:
    a = 5 / 0
except ZeroDivisionError:
    print("zero division")

try:
    a = 5 / alma  # igen tudom hogy nincs még deffiniálva
except NameError:
    print("nincs ilyen változo")

try:
    sys.exit(0)  # igen tudom hogy nincs beimportálva
    print(a)
except NameError:
    print("nincs ilyen import")

try:
    a = [1, 2]
    print(a[3])
except IndexError:
    print("nincs ilyen index")

try:
    a = {1: 'alma'}
    print(a[3])
except KeyError:
    print("nincs ilyen kulcs")

try:
    a = "alma"
    a.__floor__() # tudom hogy nincs ilyen függvény
except AttributeError:
    print("ez csak int-re működik")

try:
    a = "alma"
    b = "körte"
    print(a * b) # igen, nem lehet szozozni

except TypeError:
    print("a szorzás nem mehet string-re")
