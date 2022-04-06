def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
        
    return True

def sarake_oikein(sudoku: list, sarake: int):
    lista = []
    for rivi in sudoku:
        if rivi[sarake] > 0 and rivi[sarake] in lista:
            return False
        else:
            lista.append(rivi[sarake])

    return True

def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    luvut = []
    for r in range(rivi, rivi + 3):
        print()
        for s in range(sarake, sarake + 3):
            luku = sudoku[r][s]
            print(luku, end=" ")
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)

    return True

def sudoku_oikein(sudoku: list):
    for i in range(0, 7, 3):
        for x in range(0, 7, 3):
            if not nelio_oikein(sudoku, i, x):
                return False
    for i in range(9):
        if not (rivi_oikein(sudoku, i) and sarake_oikein(sudoku, i)):
            return False

    return True

if __name__ == "__main__":
    
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_oikein(sudoku))

    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))
    
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))