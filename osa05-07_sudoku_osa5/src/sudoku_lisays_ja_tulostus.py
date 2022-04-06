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

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    sudoku[rivi_nro][sarake_nro] = luku

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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)
    print()


    # Pelikentän muotoilu
    #while luku < i:
    #    for r in range(rivi, rivi + 3):
    #        print(end = " ")
    #        for s in range(sarake, sarake + 3):
    #            print(pelikenttä[r][s], end=" ")
    #    rivi += 3
    #    if rivi == 9:
    #        print()
    #        rivi = 0
    #        sarake += 3
    #    luku += 1
    #    print()