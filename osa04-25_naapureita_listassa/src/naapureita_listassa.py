def pisin_naapurijono(lista: list):
    n = len(lista)
    laske = 0
    perakkain = 0
    for i in range(n - 1):
        if abs(lista[i] - lista[i + 1]) == 1:
            laske += 1
        else:
            laske = 0
        if laske > perakkain:
            perakkain = laske
    return perakkain + 1

if __name__ == "__main__":
    lista_1 = [1, 2, 3, 5, 6, 9, 10] # (1, 2, 3)
    lista_2 = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    lista_3 =  [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]
    print(pisin_naapurijono(lista_1)) # 3
    print(pisin_naapurijono(lista_2)) # 4
    print(pisin_naapurijono(lista_3)) # 7