def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"

    cislo = int(cislo)
    if cislo == 0:
        return "0"
    for i in range(16):
        m = 2 ** i
        if m > cislo:
            pow = i - 1
            break
        result = ""
    for i in range(pow, -1, -1): # - 1 dělá jakoby opačný cyklus, jde to od pow až do 0
        m = 2**i
        if cislo >= m:
            result += "1"
            cislo -= m
        else:
            result += "0"
    return result


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

if __name__ == "__main__":
    vysledek1 = dec_to_bin(120)
    print(vysledek1)