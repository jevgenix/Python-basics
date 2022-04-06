def uniikit(lista: list):
    lista = sorted(lista)
    uni = []
    print(lista)
    s = 0
    for i in lista:
        print("Listan alkion arvo on:", i, f"Listan alkion numero on lista[{s}]")
        s += 1
        if i in uni:
            print(f"{i} ei ole enää uniikki, SKIP!")
        else:
            print("Lisätään uuden uniikki arvon listaan:",i)
            uni.append(i)
    return uni
if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]