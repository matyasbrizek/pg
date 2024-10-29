def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    start = figurka["pozice"]
    
    def is_within_bounds(pos):
        """Check if the position is within chess board bounds (1-8 for both row and column)."""
        row, col = pos
        return 1 <= row <= 8 and 1 <= col <= 8

    def is_path_clear(start, cil, direction):
        """Check if the path between start and target is clear in a specified direction."""
        row, col = start
        while (row, col) != cil:
            row += direction[0]
            col += direction[1]
            if (row, col) in obsazene_pozice and (row, col) != cil:
                return False
        return True

    if not is_within_bounds(cilova_pozice):
        return False

    row_diff, col_diff = abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])

    if typ == "pěšec":
        if start[1] == cilova_pozice[1]:  # Rovnoběžně
            if cilova_pozice[0] == start[0] + 1 and cilova_pozice not in obsazene_pozice:
                return True
            if start[0] == 2 and cilova_pozice[0] == start[0] + 2 and {(start[0] + 1, start[1]), cilova_pozice}.isdisjoint(obsazene_pozice):
                return True
        return False

    elif typ == "jezdec":
        return (row_diff, col_diff) in {(2, 1), (1, 2)} and cilova_pozice not in obsazene_pozice

    elif typ == "věž":
        if row_diff == 0 or col_diff == 0:
            direction = (0 if row_diff == 0 else (cilova_pozice[0] - start[0]) // row_diff,
                         0 if col_diff == 0 else (cilova_pozice[1] - start[1]) // col_diff)
            return is_path_clear(start, cilova_pozice, direction)

    elif typ == "střelec":
        if row_diff == col_diff:
            direction = ((cilova_pozice[0] - start[0]) // row_diff, (cilova_pozice[1] - start[1]) // col_diff)
            return is_path_clear(start, cilova_pozice, direction)

    elif typ == "dáma":
        if row_diff == col_diff or row_diff == 0 or col_diff == 0:
            if row_diff == col_diff:
                direction = ((cilova_pozice[0] - start[0]) // row_diff, (cilova_pozice[1] - start[1]) // col_diff)
            else:
                direction = (0 if row_diff == 0 else (cilova_pozice[0] - start[0]) // row_diff,
                             0 if col_diff == 0 else (cilova_pozice[1] - start[1]) // col_diff)
            return is_path_clear(start, cilova_pozice, direction)

    elif typ == "král":
        return row_diff <= 1 and col_diff <= 1 and cilova_pozice not in obsazene_pozice

    return False

# Testovací kód
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    test_results = {
        "pesec (3, 2)": je_tah_mozny(pesec, (3, 2), obsazene_pozice),  # True
        "pesec (4, 2)": je_tah_mozny(pesec, (4, 2), obsazene_pozice),  # False
        "pesec (1, 2)": je_tah_mozny(pesec, (1, 2), obsazene_pozice),  # False
        "jezdec (4, 4)": je_tah_mozny(jezdec, (4, 4), obsazene_pozice),  # False
        "jezdec (5, 4)": je_tah_mozny(jezdec, (5, 4), obsazene_pozice),  # False
        "jezdec (1, 2)": je_tah_mozny(jezdec, (1, 2), obsazene_pozice),  # True
        "jezdec (9, 3)": je_tah_mozny(jezdec, (9, 3), obsazene_pozice),  # False
        "dama (8, 1)": je_tah_mozny(dama, (8, 1), obsazene_pozice),      # False
        "dama (1, 3)": je_tah_mozny(dama, (1, 3), obsazene_pozice),      # False
        "dama (3, 8)": je_tah_mozny(dama, (3, 8), obsazene_pozice),      # True
    }
print(test_results)