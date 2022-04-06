def vanhin(henkilot: list):
    vuosi = henkilot[0][1]
    nimi = henkilot[0][0]
    for i in range(len(henkilot)):
        for y in range(len(henkilot[i])):
            if y == 1:
                if vuosi > henkilot[i][y]:
                    vuosi = henkilot[i][y] 
                    nimi = henkilot[i][0]
    return nimi



if __name__ == "__main__":
    
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))