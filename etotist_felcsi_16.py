# Írj egy logikai értékkel visszatérő Python függvényt, amely paraméterként kap egy egész számot és eldönti a számról,
# hogy osztható-e 2-vel és 3-mal is egyszerre! A programodban hívd is meg ezt az alprogramot!

def com_div(number):
    result = True
    if number % 2 != 0 and number % 3 != 0:
        result = False
    return result


if __name__ == '__main__':
    feed_me = input("Ezt a számot még megeszed? ")
    try:
        print(com_div((int(feed_me))))
    except ValueError:
        print("Fújj, ez nem egész szám!")
