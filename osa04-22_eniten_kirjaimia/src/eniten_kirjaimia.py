# tee ratkaisu tänne
def eniten_kirjainta(sana: str):
    merkki = 0
    kirjain = ""
    for i in sana:
        if merkki == 0 or sana.count(i) > merkki:
            merkki = sana.count(i)
            kirjain = i
    return kirjain

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))

    kolmas_jono = "aaabb"
    print(eniten_kirjainta(kolmas_jono))