luettelo = {}
while True:
    kommento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    if kommento == 3:
        print("lopetetaan...")
        break
    if kommento == 2:
        nimi = input("nimi: ")
        numero = input("numero: ")
        luettelo[nimi] = numero
        print("ok!")
    if kommento == 1:
        nimi = input("nimi: ")
        if nimi not in luettelo:
            print("ei numeroa")
        else:
            print(luettelo[nimi])