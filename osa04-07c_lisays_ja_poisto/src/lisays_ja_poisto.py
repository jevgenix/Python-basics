# Kirjoita ratkaisu tähän
lista = []
i = 1

while True:
    print("Lista on nyt", lista)
    valitse = input("(l)isää, (p)oista vai e(x)it: ")
    if valitse == "l":
        lista.append(i)
        i += 1
    if valitse == "p":
        lista.pop(len(lista) - 1)
        i -= 1
    if valitse == "x":
        break
print("Moi!")