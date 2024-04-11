# Írj egy Python eljárást, amely paraméterként kap egy egész
# számot és kiírja a képernyőre az ennél kisebb értékű elemeit a Fibonacci sornak!

def fibo_smaller(number):
    result = "0 1"
    p1, p2 = 0, 1
    jump_out = True

    # while True
    while jump_out:
        sp = p1 + p2
        p1 = p2
        p2 = sp
        if number > sp:
            result += " " + str(sp)
        else:
            jump_out = False
            # break

    return result


if __name__ == '__main__':
    ask = input("Kérem szépen azt a számot, hammm: ")
    try:
        print(fibo_smaller((int(ask))))
    except ValueError:
        print("Csak egész számot eszek, nem vagyok keto paleo!!!")
