# funkce vrati treti prvek ze seznamu
#def vrat_treti(seznam):
    #if len(seznam) < 3:
        #return None
    #else:
        #return seznam[2]

# funkce spocita prumer z hodnot v seznamu
#def udelej_prumer(seznam):
    #soucet = sum(seznam)
    #pocet_prvku = len(seznam)
    #prumer = soucet / pocet_prvku
    #return prumer

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    prumer = sum(slovnik["znamky"]) / len(slovnik["znamky"])
    jmeno = slovnik["jmeno"]
    prijmeni = slovnik["prijmeni"]
    vek = slovnik["vek"]
    return f"Jmeno: {jmeno}, Prijmeni: {prijmeni}, Vek: {vek}, Prumerna znamka: {prumer}"


if __name__ == "__main__":
    #seznam = [9,8,7]
    #vysledek = vrat_treti(seznam)
    #print(vysledek)

    #obalka = [9,8,7,6,5]
    #vysledek = udelej_prumer(obalka)
    #print(vysledek)


    #print(udelej_prumer([9,8,7,6,5]))
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))