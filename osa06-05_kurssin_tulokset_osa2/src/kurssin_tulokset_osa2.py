opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("koepisteet: ")

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

for nro, maara in tehtavat.items():
    yht = pisteet[nro] + tehtavien_lkm_pisteiksi(maara)
    print(f"{opiskelijat[nro]} {arvosana(yht)}")