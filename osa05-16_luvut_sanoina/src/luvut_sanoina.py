def lukukirja():
    sanakirja = {}
    numerot = []
    for alku in range(100):
        numerot.append(alku)

    lukusana = [
    'nolla', 'yksi', 'kaksi', 'kolme','neljä', 'viisi', 'kuusi','seitsemän', 'kahdeksan', 'yhdeksän','kymmenen']
    for luku in range(1, 10):
        lukusana.append(f"{lukusana[luku]}toista")
    
    for i in range(2, 10):
        lukusana.append(lukusana[i] + "kymmentä")
        for j in range(1, 10):
            lukusana.append(lukusana[i] + "kymmentä" + lukusana[j])

    for luku in numerot:
        if luku not in sanakirja:
            sanakirja[luku] = lukusana[luku]

    for x in sanakirja:
        print(x)
    
    return sanakirja

if __name__ == "__main__":
    luvut = lukukirja()
    for i in range(100):
        print(luvut[i], end=" ")
