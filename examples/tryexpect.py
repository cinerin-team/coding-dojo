x = input("mondj egy számot\n")
try:
    a = int(x)
    print("ez egy szam")
except ValueError:
    raise Exception("ez egy string")
else:
    print("ha nem volt hiba akkor ez is lesz")
finally:
    print("ez akkor is kiirodik ha volt hiba és akkor is ha nem")
