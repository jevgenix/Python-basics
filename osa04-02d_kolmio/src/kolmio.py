# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    if len(merkkijono) > 0:
        print(leveys * merkkijono[0])
    else:
        print(leveys * "*")


def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0
    while i < koko:
        i += 1
        viiva(i, "#")
        

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(3)


def pienin(a,b):
    if a < b:
        return a
    return b

print(pienin(3, 7))
print(pienin(5, 2))
