a = "Alma"
aa = 3
aaa = 1.3
A = ["alma", 'körte']
b = {"a": "alma", 1: 'körte', 'barmi': A}
c = set(A)

print('a')
print(type(a))
print(a)
print(a[2])
print(len(a))
print(a + "körte")

print('aa')
print(type(aa))
print(aa)
print(aa + 1)
print(7)
print(7 / 2)  # osztás (int->float)
print(7 % 2)  # maradék az osztásbóé
print(7 // 2)  # egész rész az osztásból
print(aa * 2)  # szorzás
print(aa ** 2)  # hatványozás

print('aaa')
print(type(aaa))
print(aaa)
print(aaa + 1)
print(aaa - 0.3)  # float marad

print('A')
print(A)
print(type(A))
print(A[1])
for i in A:
    print(i)
for i in range(len(A)):
    print(A[i])
A.append("cékla")
# A[len(A)] = "eper" ez pl nem jó, még ha a len jó értéket ad ki és olyan elem még nincs a listát így nem lehet bővíteni
print(A)
A[2] = 'dió'  # átírni lehet a céklát dióra
print(A)
A.remove("körte")
print(A)

print("b")
print(b)
print(type(b))
for i in b.keys():
    print(str(i) + ":" + str(b[i]))
print(b[1])
print(b['barmi'])
print("keys:")
for i in b.keys():
    print(i)
print("values:")
for i in b.values():
    print(i)
b['mindegy'] = "ezzel"
for i in b.keys():
    print(str(i) + ":" + str(b[i]))

print('c')
print(type(c))
print(c)
c.add('alma')
print(c)
c.remove('alma')
print(c)