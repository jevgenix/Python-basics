# Kirjoita ratkaisu tähän
lista = []
while True:
    sana = input("sana: ")
    if sana in lista:
        break
    lista.append(sana)
print(f"Annoit {len(lista)} eri sanaa")