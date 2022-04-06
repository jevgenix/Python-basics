from random import sample
from string import ascii_lowercase

def luo_salasana(pituus: int):    
    lista = sample(ascii_lowercase, pituus)
    salasana = ''
    for i in lista: 
        salasana += i
    return salasana

if __name__ == '__main__':
    for i in range(10):
        print(luo_salasana(8))
