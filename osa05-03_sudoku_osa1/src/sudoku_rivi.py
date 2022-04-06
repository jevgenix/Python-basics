"""def rivi_oikein(sudoku: list, rivi_nro: int):
    lista = [sudoku[rivi_nro]]
    testi = []
    for ruutu in lista:
        for alkio in ruutu:
            if alkio > 0:
                testi.append(alkio)
    testi.sort()
    for luku in range(len(testi) - 1):
        if testi[luku] == testi[luku + 1]:
            return False
    return True """
                
def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
    return True
 
if __name__ == "__main__":
    sudoku = [
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

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))