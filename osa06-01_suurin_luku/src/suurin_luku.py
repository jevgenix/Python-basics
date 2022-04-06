def suurin():
    with open("luvut.txt") as tiedosto:
        luku = 0
        lista = []
        for arvo in tiedosto:
            lista.append(int(arvo))

        for arvo in lista:
            if arvo > luku:
                luku = arvo
    return luku


if __name__ == "__main__":
    
    print(suurin())