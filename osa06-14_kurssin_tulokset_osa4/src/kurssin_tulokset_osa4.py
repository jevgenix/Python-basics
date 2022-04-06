if True:
    opiskelijatiedot = input("opiskelijatiedot: ")
    tehtavatiedot = input("tehtävätiedot: ")
    koepisteet = input("koepisteet: ")
    kurssitiedot = input("Kurssitiedot: ")
else:
    i = 2
    opiskelijatiedot = f"opiskelijat{i}.csv"
    tehtavatiedot = f"tehtavat{i}.csv"
    koepisteet = f"koepisteet{i}.csv"
    kurssitiedot = f"kurssi{i}.txt"

def arvosana(pisteet):
    a = 0
    rajat = [15, 18, 21, 24, 28]
    while a < 5 and pisteet >= rajat[a]:
        a += 1
    return a

def tehtavien_lkm_pisteiksi(lkm):
    return lkm // 4

opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimi = osat[1] + " " + osat[2].strip()
        opiskelijat[osat[0]] = nimi

tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        arvo = 0
        for t in range(1, len(osat)):
            arvo += int(osat[t])
        tehtavat[osat[0]] = arvo

pisteet = {}
with open(koepisteet) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        arvo = 0
        for p in range(1, len(osat)):
            arvo += int(osat[p])
        pisteet[osat[0]] = arvo

with open(kurssitiedot) as tiedosto:
    sisalto = tiedosto.read()
    sisalto = sisalto.replace("\n", ': ')
    osat = sisalto.split(': ')
    laajus = osat[1] + ", " + osat[3] + " opintopistettä\n"
    merkki = '=' * (len(laajus) -1)
    otsikko = f"{laajus}{merkki}\n"

nimet_tulot = {}
with open('tulos.txt', 'w') as tiedosto:
    tiedosto.write(otsikko)
    tiedosto.write("nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana\n")
    for nro, maara in tehtavat.items():
        yht = pisteet[nro] + tehtavien_lkm_pisteiksi(maara)
        nimi = opiskelijat[nro]
        teht_lkm = tehtavat[nro]
        teht_p = tehtavien_lkm_pisteiksi(tehtavat[nro])
        koe_p = pisteet[nro]
        yht_p = teht_p + koe_p
        tulos = arvosana(yht)
        nimet_tulot[nimi] = tulos
        tiedosto.write(f"{nimi:30}{teht_lkm:<10}{teht_p:<10}{koe_p:<10}{yht_p:<10}{tulos}\n")

with open('tulos.csv', 'w') as tiedosto:
    for koodi, nimi in opiskelijat.items():
        tiedosto.write(f"{koodi};{nimi};{nimet_tulot[nimi]}\n")