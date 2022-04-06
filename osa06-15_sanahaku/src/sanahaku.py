def hae_sanat(hakusana: str):
    sanalista = []
    with open('sanat.txt') as tiedosto:
        sisalto = tiedosto.read()
        rivi = sisalto.split()

        if hakusana.endswith("*"):
            for sana in rivi:
                if sana.startswith(hakusana[0: len(hakusana) -1]):
                    sanalista.append(sana)
        elif hakusana.startswith("*"):
            for sana in rivi:
                if sana.endswith(hakusana[1:]):
                    sanalista.append(sana)
        else:
            for sana in rivi:
                if len(sana) == len(hakusana):
                    tarkista1 = []
                    tarkista2 = []
                    for i in range(len(hakusana)):
                        if hakusana[i] == '.':
                            continue
                        tarkista1.append(hakusana[i])
                        tarkista2.append(sana[i])
                    if tarkista1 == tarkista2 and sana not in sanalista:
                        sanalista.append(sana)
    return sanalista

if __name__ == "__main__":
    print(hae_sanat("y..i"))