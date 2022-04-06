while True:
    print('1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu')
    valinta = int(input("Valinta: "))

    if valinta == 1:
        with open('sanakirja.txt', 'a') as tiedosto:
            sana_fi = input('Anna sana suomeksi: ')
            sana_eng = input('Anna sana englanniksi: ')
            tiedosto.write(f"{sana_fi} - {sana_eng}\n")
            print('Sanapari lisätty')

    elif valinta == 2:
        with open('sanakirja.txt') as tiedosto:
            haettavat = {}
            hakusana = input('Anna sana: ')
            for rivi in tiedosto:
                rivi = rivi.replace('\n', '')
                if hakusana in rivi:
                    osat = rivi.split(' - ')
                    haettavat[osat[0]] = osat[1]
            for fi, eng in haettavat.items():
                print(f"{fi} - {eng}")
    else:
        print("Moi!")
        break
