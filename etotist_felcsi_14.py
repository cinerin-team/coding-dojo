#Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*)
# karaktereket M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)!
# A programodban hívd is meg ezt az alprogramot!

def print_out_stars(num1, num2):
    result = ""
    for i in range(num1):
        for j in range(num2):
            result += "*"
        result += "\n"
    return result

if __name__ == '__main__':
    ask1 = input("Kérem szépen (de nagyon szépen) az első számot: ")
    ask2 = input("Kérem szépen (de k*rva szépen) a második számot: ")
    try:
        print(print_out_stars(int(ask1), int(ask2)))
    except ValueError:
        raise Exception("\nNem tudod hogy mi az a szám, te ******?")
