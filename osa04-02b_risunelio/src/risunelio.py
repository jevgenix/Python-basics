# kopioi edellisestä tehtävästä funktion viiva koodi tänne
# tee ratkaisu tänne
def viiva(leveys, merkkijono):
    if len(merkkijono) > 0:
        print(leveys * merkkijono[0])
    else:
        print(leveys * "*")


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = koko
    while i > 0:
        viiva(koko, "#")
        i -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(3)
