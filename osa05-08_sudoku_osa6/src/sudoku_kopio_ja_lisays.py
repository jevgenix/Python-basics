def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    
    """
    uusi = []
    for r in sudoku:
        uusi.append(r[:])
 
    uusi[rivi_nro][sarake_nro] = luku
    return uusi
    """
    kopio = []
    for r in sudoku:
        rivi = []
        for i in r:
            rivi.append(i)
        kopio.append(rivi)
    
    kopio[rivi_nro][sarake_nro] = luku
    return kopio


def tulosta(sudoku: list):
    # Muuttujat
    rivi = 0
    sarake = 0
    #Jos alkion arvo on 0: sen arvoksi "_"
    for r in range(9):
        for s in range(9):
            if sudoku[s][r] == 0:
                sudoku[s][r] = "_"
    # kopioidan lista
    pelikenttä = sudoku[:]
    for rivi in range(9):
        if rivi > 0 and rivi % 3 == 0:
            print()
        for sarake in range(0, 9):
            print(pelikenttä[rivi][sarake], end=" ")
            if (sarake + 1) % 3 == 0:
                print(end=" ")
        print()



if __name__ == "__main__":
    
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)