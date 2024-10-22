def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.
    """
    nove_cislo = int(cislo)

    # Pokud je cislo menší nebo rovno 1, není prvočíslo
    if nove_cislo <= 1:
        return False
    # Pokud je cislo 2, je prvočíslo
    elif nove_cislo == 2:
        return True
    # Pokud je cislo sudé, není prvočíslo
    elif nove_cislo % 2 == 0:
        return False
    # Kontrola dalších dělení až do odmocniny čísla
    else: 
        i = 3
        while i * i <= nove_cislo:
            if nove_cislo % i == 0:
                return False
            i += 2
        return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    maximum = int(maximum)
    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla

if __name__ == "__main__":
    maximum = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(maximum)
    print(prvocisla)
    
