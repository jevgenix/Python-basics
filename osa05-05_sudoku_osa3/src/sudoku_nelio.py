def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    lista = []
    r = 0
    a = 0
    #mihin = sudoku[rivi + r][sarake + a]
    for i in range(9):
        lista.append(sudoku[rivi + r][sarake + a])
        a += 1
        if a == 3:
            r += 1
            a = 0
    luvut = []
    for luku in lista:
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



    print(nelio_oikein(sudoku, 0, 0))
    print(nelio_oikein(sudoku, 1, 2))
    
    


































