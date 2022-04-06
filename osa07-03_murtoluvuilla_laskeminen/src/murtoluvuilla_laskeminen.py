
from fractions import *
def jaa_palasiksi(maara: int):
    list = []
    for i in range(maara):
        list.append(Fraction(1, maara))
    return list

if __name__ == '__main__':
    for p in jaa_palasiksi(3):
        print(p)

    print()

    print(jaa_palasiksi(5))

    print(0.1 + 0.2 == 0.3)