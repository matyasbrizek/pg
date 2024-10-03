#prvni funkce
def hello():
    print("Hello World!")

#hello()


#funkce, která určí, jestli číslo je sudé nebo liché
def sudy_nebo_lichy(cislo):
    vysledek = cislo % 2

    if vysledek == 0:
        print("Číslo ", cislo, " je sudé")
    else:
        print("Číslo ", cislo, " je liché")

sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)