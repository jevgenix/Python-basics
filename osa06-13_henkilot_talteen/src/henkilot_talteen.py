def tallenna_henkilo(henkilo: tuple):
    with open('henkilot.csv', 'w') as tiedosto:
        nimi = henkilo[0]
        ika = int(henkilo[1])
        pituus = float(henkilo[2])
        tiedosto.write(f"{nimi};{ika};{pituus}") 

if __name__ == '__main__':
    tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))