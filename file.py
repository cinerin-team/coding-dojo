f = open("testfile.txt", "r")
print(f.read())

f = open("testfile.txt", "r")
for x in f:
    print(x)

f = open("testfile.txt", "r")
print(f.readline())
f.close()
