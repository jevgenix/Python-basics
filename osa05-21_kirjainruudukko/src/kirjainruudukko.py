from string import ascii_uppercase
aakkoset = ascii_uppercase

kerrokset = 3 #int(input("kerrokset: "))


for i in range(kerrokset):
    i = 1
    print()
    aakkonen = ''

    for y in range(len(aakkoset)):
        if aakkoset[kerrokset - i] == 'Z':
            break
        print(aakkoset[kerrokset - i] * 3, end="")
        i += 1
        