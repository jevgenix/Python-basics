from random import choice, shuffle
from string import ascii_lowercase, digits
def luo_hyva_salasana(pituus: int, numb: bool, punct: bool):
    lista = []
    merkit = list('!?=+-()#')
    hyva_salasana = ''
    salasana = ''

    for i in range(pituus):
        lista.append(choice(ascii_lowercase))
        if numb:
            lista.append(choice(digits))
        if punct:
            lista.append(choice(merkit))
    
    for i in range(pituus):
        hyva_salasana += lista[i]
    
    salasana = list(hyva_salasana)
    shuffle(salasana)
    hyva_salasana =''.join(salasana)
    
    return hyva_salasana

if __name__ == '__main__':    
    print(luo_hyva_salasana(18, True, True))
