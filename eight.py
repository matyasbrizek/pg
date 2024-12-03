def bin_to_dec(binarni_cislo):
    # Funkce spočítá hodnotu předávaného binárního čísla (binarni_cislo může být str i int)
    # Převést na řetězec (pokud již není)
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    
    # Algoritmus převodu z binární do desítkové soustavy
    decimalni_hodnota = 0
    for i, bit in enumerate(reversed(binarni_cislo)):  # Procházíme číslo odzadu
        if bit == '1':  # Pouze pokud je bit 1, přičítáme odpovídající hodnotu
            decimalni_hodnota += 2 ** i  # Přičíst hodnotu podle mocniny dvou
    return decimalni_hodnota

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128