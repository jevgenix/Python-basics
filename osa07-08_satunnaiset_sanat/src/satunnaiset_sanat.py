from random import sample
def sanat(n: int, alku: str):
    lista = []
    with open('sanat.txt') as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '')
            if rivi.startswith(alku) and rivi not in lista:
                lista.append(rivi)
    
    if len(lista) < n:
        raise ValueError("Sopivia sanoja ei löydy tarpeeksi!")
    
    return sample(lista, n)


if __name__ == '__main__':
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)