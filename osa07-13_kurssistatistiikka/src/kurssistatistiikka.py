import urllib.request, certifi, json
from math import floor

def hae_kaikki():
    osoite = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    pyynto = urllib.request.urlopen(osoite, cafile=certifi.where())
    data = json.loads(pyynto.read())
    lista = []
    for t in data:
        e = t["enabled"]
        if e == False:
            continue
        kurssin_nimi = t["fullName"]
        nimi = t["name"]
        vuosi = t["year"]
        tehtavat = sum(t["exercises"])
        t = kurssin_nimi, nimi, vuosi, tehtavat
        lista.append(t)
    return lista

def hae_kurssi(kurssi: str):
    osoite = 'https://studies.cs.helsinki.fi/stats-mock/api/courses/' + kurssi +  '/stats'
    pyynto = urllib.request.urlopen(osoite, cafile=certifi.where())
    data = json.loads(pyynto.read())
    tunnit = 0
    tehtavat = 0
    opiskelijat = 0
    for a, b in data.items():
        tunnit += b['hour_total']
        tehtavat += b['exercise_total']
        if b['students'] > opiskelijat:
            opiskelijat = b['students']
    
    tunnit_km = floor(tunnit / opiskelijat)
    teht_km = floor(tehtavat / opiskelijat)

    return {
    'viikkoja': len(data),
    'opiskelijoita': opiskelijat,
    'tunteja': tunnit,
    'tunteja_keskimaarin': tunnit_km,
    'tehtavia': tehtavat,
    'tehtavia_keskimaarin': teht_km
    }

if __name__ == "__main__":    
    print(hae_kaikki())
    print(hae_kurssi("ofs2019"))