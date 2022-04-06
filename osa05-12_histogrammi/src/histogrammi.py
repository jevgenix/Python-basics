def histogrammi(mjono: str):
    sanalista = {}
    pi = len(mjono)

    for i in range(pi):
        kirjain = mjono[i]
        if kirjain not in sanalista:
            sanalista[kirjain] = []
        sanalista[kirjain].append(kirjain)
    print(sanalista)
    for avain, arvo in sanalista.items():
        print(avain, len(arvo) * '*')




if __name__ == "__main__":
    histogrammi("saippuakauppias")