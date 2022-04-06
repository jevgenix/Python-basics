while True:
    with open("paivakirja.txt", "a") as tiedosto:
        print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
        valinta = int(input("Valinta: "))
        if valinta == 1:
            merkintä = input("Anna merkintä: ")
            tiedosto.write(f"{merkintä}\n")
            print("Päiväkirja tallennettu")
            print()
        elif valinta == 2:
            with open("paivakirja.txt") as tiedosto:
                sisalto = tiedosto.read()
                print(sisalto)
        else:
            print("Heippa!") 
            break