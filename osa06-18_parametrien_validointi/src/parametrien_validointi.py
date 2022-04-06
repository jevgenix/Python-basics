def uusi_henkilo(nimi: str, ika: int):
    kaksi = nimi.split(" ")
    if len(nimi) == 0 or len(kaksi) < 2 or len(nimi) > 40:
        raise ValueError
    if ika < 0 or ika > 150:
        raise ValueError
    return nimi, ika

if __name__ == '__main__':
    henkilo = uusi_henkilo("pekka", 13)
    print(henkilo)