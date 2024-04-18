# Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap három számot és eldönti,
# hogy az összes paramétere pozitív-e! A programodban hívd is meg ezt az alprogramot!

def all_three_pos(num1, num2, num3):
    result = False
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        result = True
    return result


if __name__ == '__main__':
    three_nums_1 = input("Nagyon szépen kérlek Téged, drága lelkem, egy darab egész számot pötyögj be nekem, köszike: ")
    three_nums_2 = input("Nagyon szépen kérlek Téged, drága lelkem, ismételten egy darab egész számot pötyögj be nekem, puszika: ")
    three_nums_3 = input("Látom ez már megy! Kérlek Téged, aranyoskám, egy darab egész számot pötyögj be nekem megint, dánke: ")
    try:
        print(all_three_pos((int(three_nums_1)), int(three_nums_2), int(three_nums_3)))
    except ValueError:
        print("Really? -_- Am I a joke to you? https://hu.wikipedia.org/wiki/Eg%C3%A9sz_sz%C3%A1mok")
