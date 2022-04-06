def lisaa_opiskelija(sanakirja: dict, nimi: str):
    sanakirja[nimi] = ""
    return sanakirja

def lisaa_suoritus(sanakirja: dict, nimi: str, suoritus: tuple):
    testi = []
    lista_tuple = []
    if sanakirja[nimi] == "ei suorituksia" or sanakirja[nimi] == "":
        sanakirja[nimi] = []
        
    sanakirja[nimi].append(tuple(suoritus))
    kopio = sorted(sanakirja[nimi])[::-1]
    
    for avain, arvo in sanakirja.items():
        if arvo == "":
            continue
        
    for aine, arvosana in kopio:
        if aine not in testi and arvosana > 0:
            testi.append(aine)
            testi.append(arvosana)
    
    for i in range(len(testi) - 1):
        monikko = testi[i], testi[i + 1]
        if monikko not in lista_tuple and i % 2 == 0:
            lista_tuple.append(monikko)
        
    sanakirja[nimi] = lista_tuple[::-1].copy()
    
    return sanakirja

def tulosta(sanakirja: dict, nimi: str):
    oletus = "ei suorituksia"
    if nimi in sanakirja:
        print(f"{nimi}:")
        
        if sanakirja[nimi] == "":
            sanakirja[nimi] = oletus
            print(" " + sanakirja[nimi])
        
        else:
            if len(sanakirja[nimi]) > 0:
                keskiarvo = 0
                print(" suorituksia", len(sanakirja[nimi]), "kurssilta:")
                for avain, arvo in sanakirja[nimi]:
                    print(f"  {avain} {arvo}")
                    keskiarvo += arvo
                if keskiarvo > 0:
                    keskiarvo = keskiarvo / len(sanakirja[nimi])
                    print(" keskiarvo", keskiarvo)
            else:
                print(" ei suorituksia")
    else:
        print("ei löytynyt ketään nimellä", nimi)

def kooste(opiskelijat: dict):
    monta = 0
    eniten = 0
    nimi = ""
    ka = 0
    ka_oikea_nimi = ""
    ka_kopio = 0
    ka_nimi = ""
    for avain, arvo in opiskelijat.items():
        monta += 1
        if eniten < len(arvo):
            eniten = len(arvo)
            nimi = avain
        
        for a, b in arvo:
            ka_kopio += b
            ka_nimi = avain
        ka_kopio = ka_kopio / len(arvo)
        
        if ka < ka_kopio:
            ka = ka_kopio 
            ka_oikea_nimi = ka_nimi
        ka_kopio = 0
    
    print("opiskelijoita", monta)
    print("eniten suorituksia", eniten, nimi)
    print("paras keskiarvo", ka, ka_oikea_nimi)
        
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