from datetime import datetime, timedelta
import csv
# nimi; tehtävä; pisteet ;hh:mm
#   0      1        2       3
def viralliset_pisteet():
    with open("palautus.csv") as tiedosto:
        sisa = []
        for rivi in csv.reader(tiedosto, delimiter=";"):
            pisteet = {}
            nimi = rivi[0]
            pisteet[nimi] = [rivi[1], rivi[2], rivi[3]]
            sisa.append(pisteet)
        sisa = poista_huijarit(sisa)
        return kasittely(sisa)

def poista_huijarit(ajat: dict):
    with open("tentin_aloitus.csv") as aloitus:
        ilman_huijareita = []
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[1], "%H:%M")
            for alkio in ajat:
                for tunnus, tiedot in alkio.items():
                    if nimi == tunnus:
                        if (datetime.strptime(tiedot[2], "%H:%M") - aika) > timedelta(hours=3):
                            continue
                        oikeat = {}
                        oikeat[tunnus] = tiedot
                        if oikeat not in ilman_huijareita:
                            ilman_huijareita.append(oikeat)
        return ilman_huijareita

def kasittely(tieto: dict):
    # [{tunnus : {1: pisteet, 2: pisteet, 3: pisteet...}}]
    with open('tentin_aloitus.csv') as tiedosto:
        luettelo = {}
        for rivi in csv.reader(tiedosto, delimiter=";"):
            nimi = rivi[0]
            luettelo[nimi] = {}
            for sanakirja in tieto:
                for tunnus, tiedot in sanakirja.items():
                    t_numero = tiedot[0]
                    t_pisteet = tiedot[1]

                    if rivi[0] == tunnus:
                        if t_numero not in luettelo[tunnus]:
                            luettelo[nimi][t_numero] = t_pisteet
                        if int(t_pisteet) > int(luettelo[tunnus][t_numero]):
                            luettelo[nimi][t_numero] = t_pisteet
    
    lopulliset_pisteet = {}
    print(luettelo["tiina"])
    for tunnus, tehtava in luettelo.items():
        summa = 0
        for t_numero, arvosana in tehtava.items():
            summa += int(arvosana)
        lopulliset_pisteet[tunnus] = summa
    return lopulliset_pisteet
    
if __name__ == '__main__':
    viralliset_pisteet()