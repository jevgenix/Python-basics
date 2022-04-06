# kopioi edellisestä tehtävästä funktion viiva koodi tänne
# tee ratkaisu tänne
def viiva(leveys, merkkijono):
    if len(merkkijono) > 0:
        print(leveys * merkkijono[0])
    else:
        print(leveys * "*")


def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    
    while korkeus > 0:
        viiva(10, "#")
        korkeus -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
