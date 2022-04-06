# Kirjoita ratkaisu tähän
i = 1
lista = []
monta = int(input("Kuinka monta lukua: "))
while True:
    lukuja = int(input(f"Anna luku {i}:"))
    i += 1
    lista.append(lukuja)
    if monta < i:
        print(lista)
        break