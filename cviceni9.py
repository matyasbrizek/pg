def sudy_lichy(cislo):

    cisla = int(cislo)
    je_sudy = ""

    if cisla % 2 == 0:
        je_sudy = "sudy"
    elif cisla == 0:
        je_sudy = "sudy"
    else:
        je_sudy = "lichy"
        
    return je_sudy


def test_sudy_lichy():
    assert sudy_lichy(2) == "sudy"
    assert sudy_lichy(35) == "lichy"
    assert sudy_lichy(5) == "lichy"
    assert sudy_lichy(20) == "sudy"
    assert sudy_lichy(8) == "sudy"

if __name__ == "__main__":
    vysledek1 = sudy_lichy(5)
    print(vysledek1)