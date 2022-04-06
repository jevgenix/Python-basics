# tee ratkaisu tänne
def summa(lista1: list, lista2: list):
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i] + lista2[i])
    return lista


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]
