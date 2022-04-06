# tee ratkaisu tänne
def pisin(lista: list):
    maksimi = 0
    for i in lista:
        if len(i) > maksimi:
            maksimi = len(i)
            sana = i
    return sana

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))