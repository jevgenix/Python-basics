# tee ratkaisu tänne
from string import punctuation, ascii_letters
def jaa_merkkeihin(merkkijono: str):
    ascii = ''
    punct = ''
    other = ''
    for index in merkkijono:
        if index in ascii_letters:
            ascii += index
        elif index in punctuation:
            punct += index
        else:
            other += index

    return ascii, punct, other

    

if __name__ == '__main__':
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])