def transponoi(matriisi: list):
    p = len(matriisi)
    for r in range(p):
        for s in range(r, p):
            
            temp = matriisi[r][s]
            matriisi[r][s] = matriisi[s][r]
            matriisi[s][r] = temp

            # or 
            # matriisi[r][s], matriisi[s][r] = matriisi[s][r], matriisi[r][s]

    for i in matriisi:
        print(i)
            

if __name__ == "__main__":
    lista_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
    
    lista_2 = [[1,2], [1,2]]
    transponoi(lista_1)
    
    transponoi(lista_2)
    
