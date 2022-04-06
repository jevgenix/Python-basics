def matriisi(txt: str):
    matriisi = []
    with open(txt) as file:
        for rivi in file:
            luvut = []
            arvo = rivi.split(",")
            for alkio in arvo:
                luvut.append(int(alkio))
            matriisi.append(luvut)

    return matriisi

def rivisummat():
    lista = matriisi("matriisi.txt")
    matriisin_summat = []
    for i in range(len(lista)):
        luku = 0
        for j in range(len(lista[i])):
            luku += lista[i][j]
        matriisin_summat.append(luku)
    return matriisin_summat

def summa():
    arvojen_summat = rivisummat()
    return sum(arvojen_summat)
    
def maksimi():
    lista = matriisi("matriisi.txt")
    alku = True
    for index in range(len(lista)):
        for arvo in lista[index]:
            if alku or suurin < arvo:
                suurin = arvo
                alku = False
    return suurin

if __name__ == "__main__":
    lista = matriisi("matriisi.txt")
    print(lista)
    print(summa())
    print(maksimi())