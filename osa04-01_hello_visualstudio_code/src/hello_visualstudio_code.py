# Kirjoita ratkaisu tähän
"""while True:
    e = input("Editori: ")
    e = e.lower()
    if e == "visual studio code":
        break
    elif e == "word" or e == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
print("loistava valinta!")
"""
t = [1, 2, 3, 4, 5]
for luku in t:
    print(luku)

def itseisarvo(l):
    if l < 0:
        l = -l
    return l 


x = (-10)
y = (12)
itseisarvo(x)
itseisarvo(y)