from datetime import datetime, timedelta
import csv
def huijarit():
    with open("tentin_aloitus.csv") as aloitus, open("palautus.csv") as palautus:
        aloitusajat = {}
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[1], "%H:%M")
            aloitusajat[nimi] = aika

        palautusajat = {}
        for rivi in csv.reader(palautus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[3], "%H:%M")
            
            if nimi not in palautusajat:
                palautusajat[nimi] = aika

            elif aika > palautusajat[nimi]:
                palautusajat[nimi] = aika
        huijarit = []
        for nimi in aloitusajat:
            if palautusajat[nimi] - aloitusajat[nimi] > timedelta(hours = 3):
                huijarit.append(nimi)

        return huijarit
if __name__ == '__main__':
    h = huijarit()
    print(h)