# tee ratkaisu tänne
import math
def muotoile(lista: list):
    uusi = []
    for i in lista:
        uusi.append(f"{i:.2f}")
    return uusi

if __name__ == "__main__":
    
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)

    n = 1.5566               
    t = 1                  
    print(f"Luku: {n:.{t}f}")