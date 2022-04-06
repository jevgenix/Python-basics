# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(leveys, merkkijono):
    if len(merkkijono) > 0:
        print(leveys * merkkijono[0])
    else:
        print(leveys * "*")

def kuvio(asti, merkki, kertaa, mjono):
    i = 0
    s = 0
    while i < asti:
        i += 1
        viiva(i, merkki)
        if i == asti:
            while s < kertaa:
                s += 1
                viiva(asti, mjono)
        


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")
    