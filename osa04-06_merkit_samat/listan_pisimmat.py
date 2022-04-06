"""# tee ratkaisu tänne
def pisimmat(lista: list):
    lista = sorted(lista, key=len)
    lista = lista[:: -1]
    pisin = ""
    tulos = []
    for nimi in lista:
        if pisin == "" or len(nimi) >= len(pisin):
            pisin = nimi
            tulos.append(pisin)
    return tulos[:: -1]
"""
def pisimmat(nimet: list):
    lista = []
    for nimi in nimet:
        if lista == [] or len(nimi) > len(lista[0]):
            lista = [nimi]
        elif len(nimi) == len(lista[0]):
            lista.append(nimi)
    return lista

n = "moi moi!"
i = 0
for m in n:   
    print(m)   
    i += 1
print(i)

if __name__ == "__main__":
    lista = ['Leena', 'Mikko', 'Minna']
    tulos = pisimmat(lista)
    print(tulos)