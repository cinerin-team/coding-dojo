alma = "egész osztás, mint C-ben"
szotar = {}
for a in alma:
    if a in szotar.keys():
        szotar[a] += 1
    else:
        szotar[a] = 1

print(sorted(szotar.items()))

