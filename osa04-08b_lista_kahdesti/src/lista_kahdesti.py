# Kirjoita ratkaisu tähän
lista = []
while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        break
    lista.append(luku)
    sort = sorted(lista)
    print("Lista:", lista)
    print("Järjestettynä:", sort)
print("Moi!")