if False:
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
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
print(opiskelijat)
print(tehtavat)
for nro, nimi in opiskelijat.items():    
    print(f"{nimi} {tehtavat[nro]}")      