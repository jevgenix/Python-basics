# tee ratkaisu tänne
def viiva(leveys, merkkijono):
    if len(merkkijono) > 0:
        print(leveys * merkkijono[0])
    else:
        print(leveys * "*")


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "")
