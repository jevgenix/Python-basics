from difflib import get_close_matches
sanalista = []
with open("wordlist.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        sanalista.append(rivi)

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
print('\nkorjausehdotukset:')
ehdotukset = {}
for sana in lista:    
    if sana.startswith('*'):
        ehdotukset[sana[1:len(sana)-1]] = get_close_matches(sana[1:len(sana) -1 ], sanalista)

for sana, ehdotus in ehdotukset.items():
    e = ", ".join(ehdotus)
    print(f"{sana}: {e}")