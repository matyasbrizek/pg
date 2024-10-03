# funce demonstrující cyklu while

def stars_while():
    print("zacatek")

    i = 0
    while i<5:
        print("*")
        i += 1

    print("konec")


# funce demonstrující cyklu for

def stars_for():
       print("zacatek")
       
       for i in range(5):
            print("*", i)
            i += 1
            print("konec")


# funkce urcujici, zda number lezi mezi mi_number a max_number

def in_range(min_number, max_number, number):

    if number >= min_number and number <= max_number:
        print("Is in range")
    else:
        print("Is not in range")

#in_range(100, 1000, 1)


#funkce vypíše string "Ahoj jmeno"
def zobraz_pozdrav(jmeno):
    print("Ahoj", jm)

jm = input("Zadej jmeno: ")
zobraz_pozdrav(jm)