# tee ratkaisu tänne
def vaihteluvali(lista : list):
    return max(lista) - min(lista)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)
    lista = [1, 3, 5, 7, 9]
    print(lista[4])