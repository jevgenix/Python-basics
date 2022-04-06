# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    kopio = {}
    for avain, arvo in sanakirja.items():
        kopio[arvo] = avain

    sanakirja.clear()
    
    for avain, arvo in kopio.items():
        sanakirja[avain] = arvo
    
if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)