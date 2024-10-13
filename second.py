def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = [" ", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šdesát", "sedmdesát", "osmdesát", "devadesát"]
    deset_devatenact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    zadavane_cislo = int(cislo)
    
    if zadavane_cislo < 10:
        return jednotky[zadavane_cislo]
    elif zadavane_cislo >= 10 and zadavane_cislo < 20:
        return deset_devatenact[zadavane_cislo - 10]
    elif zadavane_cislo >= 20 and zadavane_cislo < 100:
        desitka = zadavane_cislo / 10
        jednotka = zadavane_cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] and " " and jednotky[jednotka]
    elif zadavane_cislo == 100:
        return "sto"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)