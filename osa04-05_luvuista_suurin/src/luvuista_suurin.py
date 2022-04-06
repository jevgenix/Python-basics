# tee ratkaisu tänne
def luvuista_suurin(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(1, 1, -1)
    print(suurin)