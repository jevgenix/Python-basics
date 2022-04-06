# tee ratkaisu tänne
def ilman_vokaaleja(sana: str):
    vokaalit = ['a', 'o', 'u', 'e', 'i', 'ä', 'ö', 'y', 'å']
    for i in vokaalit:
        sana = sana.replace(i, "")
    return sana



if __name__ == "__main__": 
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
