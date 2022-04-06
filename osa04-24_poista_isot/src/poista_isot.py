# tee ratkaisu tänne
def poista_isot(lista: list):
    pienet = []
    for i in lista:
        if not i.isupper():
            pienet.append(i)
    return pienet
    
if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)