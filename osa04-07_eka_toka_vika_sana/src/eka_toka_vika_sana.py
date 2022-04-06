# tee ratkaisu tänne
def eka_sana(eka):
    i = 0
    sana = ""
    while True:
        sana += eka[i]
        i += 1
        if " " in eka[i]:
            return sana        
    
def toka_sana(toka):
    i = (len(eka_sana(toka))) + 1
    pituus = len(toka) - len(eka_sana(toka)) - 1
    toka_sana = ""
    while True:
        toka_sana += toka[i]
        i += 1
        pituus -= 1
        if pituus == 0 or " " in toka[i]:
            return toka_sana
             
def vika_sana(vika):
    i = -1
    sana = ""
    while True:
        sana += vika[i]
        i -= 1
        if " " in vika[i]:
            return sana[::-1]

def tee_jotain(a, b):
   return b + a      

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))

    