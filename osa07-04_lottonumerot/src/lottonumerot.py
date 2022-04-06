from random import sample

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot = list(range(alaraja, ylaraja + 1))
    lotto = sample(numerot, maara)
    return sorted(lotto)

if __name__ == '__main__':
    for numero in lottonumerot(1, 1, 2):
        print(numero)