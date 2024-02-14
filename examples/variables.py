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
print(7 / 2)
print(7 % 2)
print(7 // 2)
print(aa * 2)
print(aa ** 2)

print('aaa')
print(type(aaa))
print(aaa)
print(aaa + 1)
print(aaa - 0.3)

print('A')
print(A)
print(type(A))
print(A[1])
for i in A:
    print(i)
for i in range(len(A)):
    print(A[i])
A.append("cékla")
print(A)
A[2] = 'dió'
print(A)
A.remove("körte")
print(A)
