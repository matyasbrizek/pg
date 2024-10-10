import sys

def main(soubor):
    #print(f"Parametr obsahuje'{parametr}'")
    otevreny_soubor = open(soubor, "r")
    for radka in otevreny_soubor:
        parametry = radka.split(",")
        vek = int(parametry[2])
        if vek > 20:
            print(radka)
if __name__ == "__main__":
    #jmeno = input("Zadej jmeno: ")
    #main(jmeno)
    #prijmeni = input ("Zadej prijmeni: ")
    #main(prijmeni)
    if len(sys.argv) <=1:
        print("Zadej název souboru")
        sys.exit(1)
    soubor = sys.argv[1]
    main(soubor)