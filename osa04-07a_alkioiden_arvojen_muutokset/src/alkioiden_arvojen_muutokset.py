# Kirjoita ratkaisu tähän
lista = [1, 2, 3, 4, 5]

while True:
    index = int(input("Anna indeksi: "))
    if index == -1:
        break
    arvo = int(input("Anna Arvo: "))
    lista[index] = arvo
    print(lista)