alma = "egész osztás, mint C-ben"
szotart = {}
for a in alma:
    if a in szotart.keys():
        szotart[a] += 1
    else:
        szotart[a] = 1

print(sorted(szotart.items()))

