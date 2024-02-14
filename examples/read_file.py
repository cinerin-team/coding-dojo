# egyben az egész
f = open("testfile.txt", "r")
print(f.read())
f.close()


# soronként
f = open("testfile.txt", "r")
for line in f:
    print(line)
f.close()

# soronként máshogy
with open("testfile.txt", "r") as file:
    next_line = file.readline()
    while next_line:
        print(next_line)
        next_line = file.readline()
f.close()
