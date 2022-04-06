# esimerkki
def alkukirjaimien_mukaan(lista):
    #luodaan sanalista
    ryhmat = {}
    
    #tarvittavat sanat ovat listassa
    for sana in lista:
        #alustetaan sanan alkukirjain
        alkukirjain = sana[0]
        #mikäli alkukirjain ei löyty ryhmästä (uudesta sanalistasta)
        if alkukirjain not in ryhmat:
            #luodaan lista sanaa varten
            ryhmat[alkukirjain] = []   
        # lisätään sana listaan 
        ryhmat[alkukirjain].append(sana)
    #sanalistan visualisointi:
    print(ryhmat)
    #arvon palautus
    return ryhmat




sanalista = [
  "banaani", "maito", "olut", "juusto", "piimä", "mehu", "makkara",
  "tomaatti", "kurkku", "voi", "margariini", "juusto", "makkara",
  "olut", "piimä", "piimä", "voi", "olut", "suklaa"
]

ryhmat = alkukirjaimien_mukaan(sanalista)


for avain, arvo in ryhmat.items():
    print(f"Kirjaimella {avain} alkavat sanat: ")
    for sana in arvo:
        print(sana)