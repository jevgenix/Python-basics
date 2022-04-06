if False:
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input("koepisteet: ")
else:
    opiskelijatiedot = "opiskelijat1.csv"    
    tehtavatiedot = "tehtavat1.csv"
    koepisteet = "koepisteet1.csv"

print("nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana")

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
    nimi = opiskelijat[nro]
    teht_lkm = tehtavat[nro]
    teht_p = tehtavien_lkm_pisteiksi(tehtavat[nro])
    koe_p = pisteet[nro]
    yht_p = teht_p + koe_p
    tulos = arvosana(yht)
    print(f"{nimi:30}{teht_lkm:<10}{teht_p:<10}{koe_p:<10}{yht_p:<10}{tulos}")