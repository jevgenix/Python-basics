# tee ratkaisu tänne
def lyhin(lista: list):
    lyhin = ""
    for nimi in lista:            
        if lyhin == "" or len(nimi) < len(lyhin):
            lyhin = nimi
    return lyhin

if __name__ == "__main__":
    lista = ['Arto', 'Matti']
    tulos = lyhin(lista)
    print(tulos)