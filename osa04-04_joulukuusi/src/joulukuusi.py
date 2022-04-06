# tee ratkaisu tänne
def joulukuusi(määrä):
    print("joulukuusi!")
    i = määrä - 1
    s = 1
    while määrä > 0:
        väli = määrä * " "
        print(väli[1:] + "*" * s)
        s += 2
        määrä -= 1
    print(i * " " + "*")
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)