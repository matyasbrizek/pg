def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    obvod = 4 * delka_strany
    return obvod

def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    obsah = delka_strany * delka_strany
    return obsah

def pocet_pismen(text, pismeno):
   # funkce spocita kolik je pismen v daném řetězci

   pocet = 0
   for p in text:
       if p == pismeno:
           pocet +=1

   return pocet

def index_pismene(text, pismeno):
    # funkce vrati indexy daneho pismene v textu, tzn. pro text="ahoj, honzo" a pismeno="h" vrati [1, 6]
    indexy = []
    i = 0

    while i < len(text):
        if text[i] == pismeno:
            indexy.append(i)
        i += 1
    return indexy

def fibonachi(maximum):
    #vrati fibonachiho posloupnost, pro maximum -> 5 [1, 1, 2, 3, 5] 
    result = [1, 1]
    soucet = result[-2] + result[-1]
    while soucet <= maximum:
        result.append(soucet)
        soucet = result[-2] + result[-1]
    return result

if __name__ == "__main__":
    print(obsah_ctverce(5))
    print(obsah_ctverce(5))
    print(pocet_pismen("ahoj, jak se mas?" , "a"))
    print(index_pismene("ahoj, honzo", "h"))