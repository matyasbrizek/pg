import sys

def pozpatku(text):
    text_pozpatku = ""
    for pismeno in reversed(text):
        text_pozpatku +=pismeno
    return text_pozpatku

def pozpatku2(text):
    text_pozpatku = ""
    i = len(text) - 1
    while i >= 0:
        pismeno = text[i]
        text_pozpatku += pismeno
        i -= 1
    return text_pozpatku



if __name__ == "__main__":
    pozpatku("ahoj")
    try:
        soubor = sys.argv[1]
        with open(soubor, "r") as fp:
            obsah = fp.read()
            print(obsah)
            obracene = pozpatku(obsah)
            print(obracene)
    except IndexError:
        print("Zadejte název souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")