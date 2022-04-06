# tee ratkaisu tänne
def suodata_virheelliset():
    viikot = ''
    for i in range(1, 53):
        viikot += str(i)
    arvot = ''
    for i in range(1, 40):
        arvot += str(i)
    with open('lottonumerot.csv') as tiedosto:
        oikeat = {}
        
        for rivi in tiedosto:
            kaikki = {}
            rivi = rivi.replace('\n', '')
            osat = rivi.split(';')
            kaikki[osat[0]] = osat[1]
            
            for viikko, numerot in kaikki.items():
                if viikko[7:] not in viikot:
                    continue
                sep = numerot.split(',')
                bol = True
                rep = []
                for i in sep:
                    if i not in arvot or len(sep) != 7: 
                        bol = False
                        break
                for i in sep:
                    if i not in rep:
                        rep.append(i)
                    else:
                        bol = False
                        break
                if bol == False:
                    continue
                oikeat[viikko] = numerot

    with open('korjatut_numerot.csv', 'w') as tiedosto:
        for viikko, lotot in oikeat.items():
            tiedosto.write(f"{viikko};{lotot}\n")