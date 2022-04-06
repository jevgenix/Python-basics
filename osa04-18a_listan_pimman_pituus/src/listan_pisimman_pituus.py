# tee ratkaisu tänne
def pisimman_pituus(lista: list):
        pisin = 0
        for nimi in lista:
            if len(nimi) > pisin:
                pisin = len(nimi)
        return pisin

if __name__ == "__main__":
    lista = ['Arto', 'Leena', 'Santeri', 'Kim', 'Minna']
    tulos = pisimman_pituus(lista)
    print(tulos)