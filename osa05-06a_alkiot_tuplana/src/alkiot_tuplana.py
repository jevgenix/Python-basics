# tee ratkaisu tänne
def tuplaa_alkiot(luvut: list):
    kopio = luvut[:]
    for i in range(len(kopio)):
        kopio[i] = kopio[i] * 2
    return kopio


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)