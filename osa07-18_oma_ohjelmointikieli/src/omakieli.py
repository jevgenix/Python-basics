# PRINT [arvo]: tulostaa annetun arvon
# MOV [muuttuja] [arvo]: asettaa muuttujaan annetun arvon
# ADD [muuttuja] [arvo]: lisää muuttujaan annetun arvon
# SUB [muuttuja] [arvo}: vähentää muuttujasta annetun arvon
# MUL [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla
# [kohta]:: määrittelee kohdan, johon voidaan hypätä muualta
# JUMP [kohta]: hyppää annettuun kohtaan
# IF [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan
# END: lopettaa ohjelman
__author__ = 'Jekku'
__doc__ = 'Algoritmit'

def count(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total