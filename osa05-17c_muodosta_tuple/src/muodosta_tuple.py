def tee_tuple(x: int, y: int, z: int):
    moni = (x, y, z)
    pienin = min(moni)
    suurin = max(moni)
    summa = sum(moni)
    
    return (pienin, suurin, summa)
     
    
     

if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))