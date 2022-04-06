# tee ratkaisu tänne
def pelilauta():
    pelilauta = []
    for i in range(18):
        pelilauta.append([1,0,2,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0])
    return pelilauta

def kumpi_voitti(pelilauta: list):    
    
    eka = 0
    toka = 0
    for rivi in str(pelilauta):
        for ruutu in rivi:
            if "1" in ruutu:
                eka += 1
            if "2" in ruutu:
                toka += 1
    if eka > toka:
        return 1
    if toka > eka:
        return 2
    else:
        return 0

if __name__ == "__main__":
    luku = 0
    lauta = pelilauta()
    for i in lauta:
        print(i)
        print()
        luku += 1
    print("Rivejä on:", luku)
    print(kumpi_voitti(lauta))
