def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    p = len(lauta) - 1
    if (x > p or x < 0) or (y > p or y < 0):
        return False

    if lauta[y][x] == "":
        lauta[y][x] = nappula
    else:
        return False
    return True
            
if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
    
# tee ratkaisu tänne
#def tulosta(lauta: list):
    #rivi = 0
    #sarake = 0
    #print()
    #for r in range(rivi, rivi + 3):
        #for s in range(sarake, sarake + 3):
            #if lauta[r][s] == "":
            #    lauta[r][s] = "_"
            #print(lauta[r][s], end=" ")
        #print()
    #print()