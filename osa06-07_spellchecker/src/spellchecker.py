sanalista = []
with open("wordlist.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        sanalista.append(rivi)
#print(len(sanalista))

teksti = input("Write text: ")
teksti = teksti.split()

lista = []
for word in teksti:
    if word.lower() in sanalista:
        lista.append(word)
    
    else:
        word = word.replace(word, f"*{word}*")
        lista.append(word)

for sana in lista:
    print(sana, end=" ")

