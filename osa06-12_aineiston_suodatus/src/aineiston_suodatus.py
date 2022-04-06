# tee ratkaisu tänne
def suodata_laskut():
    nimet = []
    lasku = []
    laskut = []
    tulot = []
    with open("laskut.csv") as tiedosto, open('oikeat.csv', 'w') as oikeat, open('vaarat.csv', 'w') as vaarat:
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '')
            osat = rivi.split(";")
            nimet.append(osat[0])
            lasku.append(osat[1])
            if '+' in osat[1]:
                luvut = osat[1].split("+")
                summa = int(luvut[0]) + int(luvut[1])
                laskut.append(summa)
            elif '-' in osat[1]:
                luvut = osat[1].split("-")
                erotus = int(luvut[0]) - int(luvut[1])
                laskut.append(erotus)
            tulot.append(int(osat[2]))

        for i in range(len(nimet)):
            if laskut[i] == tulot[i]:
                oikeat.write(f"{nimet[i]};{lasku[i]};{tulot[i]}\n")
            else:
                vaarat.write(f"{nimet[i]};{lasku[i]};{tulot[i]}\n")
        
if __name__ == "__main__":
    suodata_laskut()