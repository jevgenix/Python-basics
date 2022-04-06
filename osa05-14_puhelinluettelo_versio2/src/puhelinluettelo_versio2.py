def hae(luettelo):
    nimi = input("nimi: ")
    if nimi not in luettelo:
        print("ei numeroa")
    else:
        for num in luettelo[nimi]:
            print(num)

def lisaa(luettelo):
    nimi = input("nimi: ")
    numero = input("numero: ")
    if nimi not in luettelo:
        luettelo[nimi] = []
    luettelo[nimi].append(numero)
    print("ok!")

def main():
    luettelo = {}
    while True:
        kommento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
        if kommento == 3:
            print("lopetetaan...")
            break
        if kommento == 2:
            lisaa(luettelo)
        if kommento == 1:
            hae(luettelo)

main()