#muj pokus
def levensteinova_vzdalenost(dotaz1, dotaz2):

    delka1 = len(dotaz1)
    delka2 = len(dotaz2)
    pismeno = 0
    cisla = 0

    if delka1 > delka2:
        for pismeno in range(0,delka2):
          if dotaz1[pismeno] == dotaz2[pismeno]:
              cisla += 0
          else:
              cisla += 1

    if delka1 < delka2:
        for pismeno in range(0,delka1):
          if dotaz1[pismeno] == dotaz2[pismeno]:
              cisla += 0
          else:
              cisla += 1
    
    
    return cisla

def levensteinova_vzdalenost2(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """
    length = max(len(dotaz1), len(dotaz2))
    i = 0
    levenstein = 0
    while i < length:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
        else:
            levenstein += 1
        i += 1
    return levenstein


def levensteinova_vzdalenost3(dotaz1, dotaz2):
    levenstein = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein
        
if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))