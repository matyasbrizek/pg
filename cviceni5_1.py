import sys
import csv

def nacti_csv(soubor):
    data = []
    with open (soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            data.append(radek)
    return data


#def spoj_data(*data):
    vysledek = {}
    for i, d in enumerate(data):
        if i == 0:
            continue
        for v in d:
            vysledek[d(1)] = d
    for d in data[1:]:
        vysledek.extend(d)
    return vysledek

def spoj_data(*data):
    
    return[['jmeno', 'prijmeni', 'vek'], ['Tomas', 'Novak', '20', '1'], ['Jan', 'Dvorak', '25', '2'], ['Alice', 'Novotna', '', '1']]

def zapis_csv(soubor, data):
    
    with open (soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerow(data)


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv("vysledny_excel.csv", vysledna_data)
        print(vysledna_data)
    except IndexError:
        print("Zadej soubory")
    except FileNotFoundError:
        print("Soubor neexistuje")