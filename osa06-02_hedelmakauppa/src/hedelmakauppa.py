# tee ratkaisu tänne
def lue_hedelmat():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            nimi = osat[0]
            hinta = osat[1]

            sanakirja[nimi] = float(hinta)
    return sanakirja



if __name__ == "__main__":
    print(lue_hedelmat())