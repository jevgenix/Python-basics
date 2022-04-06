def hae_tiedot(tiedosto: str):
    reseptikirja = {}
    reseptilista = []
    
    with open(tiedosto) as resepti_tiedosto:
        for rivi in resepti_tiedosto:
            rivi = rivi.replace('\n', '')
            reseptilista.append(rivi)
            if len(rivi) > 0:
                reseptikirja[reseptilista[0]] = reseptilista[1:]
            else:
                reseptilista = []
    
    return reseptikirja

def hae_nimi(tiedosto: str, sana: str):
    reseptikirja = hae_tiedot(tiedosto)
    resepti_nimet = []
    loydetyt_resepti_nimet = []
    
    for resepti, raakainet in reseptikirja.items():
        resepti_nimet.append(resepti)

    for reseptin_nimi in resepti_nimet:
        if sana.lower() in reseptin_nimi.lower():
            loydetyt_resepti_nimet.append(reseptin_nimi)

    return loydetyt_resepti_nimet
    
def hae_aika(tiedosto:str, aika:int):
    reseptikirja = hae_tiedot(tiedosto)
    nimi_ja_aika = []
    
    for reseptin_nimi, reseptin_tiedot in reseptikirja.items():
        if aika >= int(reseptin_tiedot[0]):
            nimi_ja_aika.append(f"{reseptin_nimi}, valmistusaika {reseptin_tiedot[0]} min")
    
    return nimi_ja_aika

def hae_raakaaine(tiedosto: str, aine: str):
    reseptikirja = hae_tiedot(tiedosto)
    lista = []
    
    for resepti, tiedot in reseptikirja.items():
        if aine in tiedot:
            lista.append(f"{resepti}, valmistusaika {tiedot[0]} min")    

    return lista

if __name__ == '__main__':
    loydetyt = hae_nimi("reseptit1.txt", "pulla")
    
    for nimi in loydetyt:
        print(nimi)

    loydetyt = hae_aika("reseptit1.txt", 20)
    
    for info in loydetyt:
        print(info)

    loydetyt = hae_raakaaine("reseptit1.txt", "maito")
    
    for resepti in loydetyt:
        print(resepti)