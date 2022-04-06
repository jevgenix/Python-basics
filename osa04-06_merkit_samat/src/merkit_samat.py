# tee ratkaisu tänne
def samat(merkkijono, a, b):
    pituus = len(merkkijono) - 1
    if b > pituus or a > pituus:
        return False
    return merkkijono[a] == merkkijono[b]
        
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 3)) 