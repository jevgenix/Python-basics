# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    arvot = {}
    for i in range(alku, loppu + 1):
        arvot[i] = i * 10
    return arvot

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)