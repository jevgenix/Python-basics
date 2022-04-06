def kaikki_vaarinpain(lista: list):
    u_list = []
    for i in lista:
        u_list.append((i[:: -1]))
    return u_list[:: -1]
if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)