from random import choice

def heita(noppa: str):
    A = 3, 3, 3, 3, 3, 6 
    B = 2, 2, 2, 5, 5, 5
    C = 1, 4, 4, 4, 4, 4
    if noppa == "A":
        return choice(A)
    elif noppa == "B":
        return choice(B)
    else:
        return choice(C)

def pelaa(noppa1: str, noppa2: str, kertaa: int):
    a = 0
    b = 0
    tasa = 0

    for i in range(kertaa):
        n1 = heita(noppa1)
        n2 = heita(noppa2)
        if n1 > n2:
            a += 1
        elif n1 < n2:
            b += 1
        else:
            tasa += 1
    return a, b, tasa

if __name__ == '__main__':

    tulos = pelaa("A", "C", 100)
    print(tulos)