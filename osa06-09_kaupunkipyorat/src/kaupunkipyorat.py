import math
def hae_asematiedot(tiedosto: str):
    asemakirja = {}
    with open(tiedosto) as asematiedot:
        for rivi in asematiedot:
            rivi = rivi.replace('\n', '')
            osat = rivi.split(';')
            if osat[0] == "Longitude":
                continue
            asemakirja[osat[3]] = float(osat[0]), float(osat[1])
    return asemakirja
    
def etaisyys(asemat: dict, asema1: str, asema2: str):
    for asema, koordinaatit in asemat.items():
        if asema1 in asema:
            x = koordinaatit
        if asema2 in asema:
            y = koordinaatit
    x_kilometreina = (x[0] - y[0]) * 55.26
    y_kilometreina = (x[1] - y[1]) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    
    return etaisyys

def suurin_etaisyys(asemat: dict):
    bol = True
    for aseman_nimi, tiedot in asemat.items():
        asema1 = aseman_nimi
        longitude1 = tiedot[0]
        latitude1 = tiedot[1]
        for toisen_a_nimi, toisen_a_tiedot in asemat.items():
            asema2 = toisen_a_nimi
            longitude2 = toisen_a_tiedot[0]
            latitude2 = toisen_a_tiedot[1]
            x_kilometreina = (longitude1 - longitude2) * 55.26
            y_kilometreina = (latitude1 - latitude2) * 111.2
            etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
            
            if bol or etaisyys > eta:
                eta = etaisyys
                aseman1_nimi = asema1
                aseman2_nimi = asema2
                bol = False
    return aseman1_nimi, aseman2_nimi, eta

if __name__ == '__main__':
    asemat = hae_asematiedot('stations3.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)
