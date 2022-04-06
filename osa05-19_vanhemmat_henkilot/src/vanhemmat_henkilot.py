def vanhemmat(henkilot: list, vuosi: int):
    lista = []
    for i in range(len(henkilot)):
        for y in range(len(henkilot[i])):
            if y == 1:
                if  henkilot[i][y] < vuosi: 
                    lista.append(henkilot[i][0])
    return lista


if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    h5 = ("Jefko", 1894)
    
    hlista = [h1, h2, h3, h4, h5]
    vanhemmat_henkilot = vanhemmat(hlista, 1979)
    print(vanhemmat_henkilot)   

    hlista_2 = [('Milla', 2014), ('Arto', 1977), ('Einari', 1985), ('Maija', 1953), ('Essi', 1997)]
    vastaus = vanhemmat(hlista_2, 2010)
    print(vastaus)