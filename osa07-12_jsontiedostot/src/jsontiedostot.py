import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as file:
        data = file.read()
    tiedot = json.loads(data)
    
    for tieto in tiedot:
        nimi = tieto["nimi"]
        ika = tieto["ika"]
        harrastus = ", ".join(tieto["harrastukset"])
        print(f'{nimi} {ika } vuotta ({harrastus})')
    

if __name__ == '__main__':
    henkilot = tulosta_henkilot('tiedosto1.json')
    print(henkilot)