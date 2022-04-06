def koepisteet_ja_harjoitus():
    pisteet = ""
    # syötetään pisteet
    while True:
        syote = input("Koepisteet ja harjoitusten määrä: ")
        # jos syöte on tyhjä, break 
        if len(syote) == 0:
            break
        # pitää olla aina väli, muuten split funktio ei toimi oikein
        pisteet += " " + syote
    pisteet = pisteet.split()
    # lista oli String muodossa, joten sen pitää vaihtaa int muotoon
    pisteet = [int(i) for i in pisteet]
    return pisteet

def tilasto():
    pisteet = koepisteet_ja_harjoitus()
    n = len(pisteet)
    # luodaan 2 eri listaa
    koe_pisteet = []
    harjoitus_pisteet = []
    for i in range(n):
        # listaan syötetään ensin koe pisteet, sitten harjoitustehtävien pisteet
        # tästä syystä mikäli listan alkio on jaollinen 2, kyseessä on koe_pisteet
        # muuten kyseessä on harjoitus_pisteet
        if i % 2 != 0:
            harjoitus_pisteet.append(pisteet[i])
        else:
            koe_pisteet.append(pisteet[i])
    # luodaan vielä yksi lista, koska täytyy prosenttien perusteella laskea pisteet
    # harjoitus_pisteet listasta
    harjoitustehtävien_arvosana = []
    for i in range(len(harjoitus_pisteet)):
        arvo = 0
        while True:
            if arvo == harjoitus_pisteet[i]:
                break
            else:
                arvo += harjoitus_pisteet[i]

        harjoitustehtävien_arvosana.append(arvo // 10)

    # summataan koe_pisteet ja harjoitustehtävien_arvosana:    
    pisteiden_summa = [koe_pisteet[i]+harjoitustehtävien_arvosana[i] for i in range(len(koe_pisteet))]
    hylätty = 0
    ykköset = 0
    kakkoset = 0
    kolmoset = 0
    neloset = 0
    vitoset = 0
    
    b = 0
    for i in koe_pisteet:
        if i < 10 and pisteiden_summa[b] < 15:
            hylätty += 1
        elif i > 9 and (pisteiden_summa[b] > 14 and pisteiden_summa[b] < 18):
            ykköset += 1
        elif i > 9 and (pisteiden_summa[b] > 17 and pisteiden_summa[b] < 21):
            kakkoset += 1
        elif i > 9 and (pisteiden_summa[b] > 20 and pisteiden_summa[b] < 24):
            kolmoset += 1
        elif i > 9 and (pisteiden_summa[b] > 23 and pisteiden_summa[b] < 28):
            neloset += 1
        elif i > 9 and pisteiden_summa[b] > 27:
            vitoset += 1
        else:
            hylätty += 1
        b += 1        

    hyväksymisprosentti = ((len(pisteiden_summa) - hylätty) / len(pisteiden_summa)) * 100 
    summa = 0
    for i in pisteiden_summa:
        summa += i
    keskiarvo = summa / len(pisteiden_summa)

    arvosanajakauma = ['0:', '1:', '2:', '3:', '4:', '5:']
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {keskiarvo:.1f}")
    print(f"Hyväksymisprosentti: {hyväksymisprosentti:.1f}")
    print("Arvosanajakauma:")
    print("  " + arvosanajakauma[-1] + " " + vitoset * "*")
    print("  " + arvosanajakauma[-2] + " " + neloset * "*")
    print("  " + arvosanajakauma[-3] + " " + kolmoset * "*")
    print("  " + arvosanajakauma[-4] + " " + kakkoset * "*")
    print("  " + arvosanajakauma[-5] + " " + ykköset * "*")
    print("  " + arvosanajakauma[-6] + " " + hylätty * "*")
        
def main():
    tilasto()

main()