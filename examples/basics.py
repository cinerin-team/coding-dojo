for i in range(5):
    print(str(i) + ". Hello")

for _ in range(5):
    print("Sima hello")

a = 2
if a == 3:
    print("a az 3")
elif a > 2:
    print("a az nagyobb mint 2")
else:
    print("a az kisebb mint 2 vagy megegyezik az értéke")

# generátorok
szamok = [2 ** n for n in range(5)]
print(szamok)

[print(2 ** n) for n in range(5)]

[print("sima hello") for _ in range(5)]

print("sum of szamok: " + str(sum(szamok)))
# print("avg of szamok: " + str(avg(szamok))) avg nincs így azt külön kell számolni
print("avg of szamok: " + str(sum(szamok)/len(szamok)))
