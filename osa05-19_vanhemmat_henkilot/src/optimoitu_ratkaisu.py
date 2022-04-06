def lisaa_opiskelija(sanakirja: dict, nimi: str):
    sanakirja[nimi] = {}

def lisaa_suoritus(sanakirja: dict, nimi: str, suoritus: tuple):
    opiskelijan_suoritus = sanakirja[nimi]
    aine = suoritus[0]
    arvosana = suoritus[1]
    
    if arvosana == 0:
        return
    
    if aine in opiskelijan_suoritus:
        if opiskelijan_suoritus[aine][1] > arvosana:
            return

    opiskelijan_suoritus[aine] = suoritus

def tulosta(sanakirja: dict, nimi: str):
    if not nimi in sanakirja:
        print("ei löytynyt ketään nimellä", nimi)
        return

    opiskelijan_suoritukset = sanakirja[nimi]
    
    print(f"{nimi}:")
    if len(opiskelijan_suoritukset) == 0:
        print(" ei suorituksia")
    else:
        keskiarvo = 0
        print(" suorituksia", len(opiskelijan_suoritukset), "kurssilta:")
        for avain, arvo in opiskelijan_suoritukset.items():
            arvosana = arvo[1]
            print(f"  {avain} {arvosana}")
            keskiarvo += arvosana
        keskiarvo = keskiarvo / len(sanakirja[nimi])
        print(" keskiarvo", keskiarvo)   

def kooste(opiskelijat: dict):
    nimi = ""
    eniten = 0
    ka = 0
    paras_ka = 0
    ka_nimi = ""
    paras_ka_nimi = ""

    for avain, arvo in opiskelijat.items():
        if eniten < len(arvo):
            eniten = len(arvo)
            nimi = avain
        for arvosana in arvo:
            numero = arvo[arvosana][1]
            ka += numero
            ka_nimi = avain

        ka = ka / len(arvo)
        if paras_ka < ka:
           paras_ka = ka 
           paras_ka_nimi = ka_nimi

        ka = 0
        
    print("opiskelijoita", len(opiskelijat))
    print("eniten suorituksia", eniten, nimi)
    print("paras keskiarvo", paras_ka, paras_ka_nimi)

if __name__ == "__main__":    
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)