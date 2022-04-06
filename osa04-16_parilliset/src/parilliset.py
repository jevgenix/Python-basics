# tee ratkaisu tänne
def parilliset(lista : list):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)