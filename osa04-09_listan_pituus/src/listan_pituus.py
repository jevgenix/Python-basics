# tee ratkaisu tänne
def pituus(lista: list):
    return len(lista)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = pituus(lista) 
    print(tulos)