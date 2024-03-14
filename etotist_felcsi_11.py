# Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre felváltva a
# 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!

def shitting_out_0_or_1(number):
    result = ""
    for i in range(number):
        if i % 2 == 1:
            result += "1"
        else:
            result += "0"
    return result


if __name__ == '__main__':
    asking = input("Kérek egy számot: ")
    try:
        print(shitting_out_0_or_1(int(asking)))
    except ValueError:
        print("mondom számot!!!!!")