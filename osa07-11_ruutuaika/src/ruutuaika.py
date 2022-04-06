from datetime import datetime, timedelta
tiedosto = input('Tiedosto: ')
with open(tiedosto, 'w') as t:
    minuutit = []
    print('Tiedosto:', tiedosto)
    startDate = input("Aloituspäivä: ")
    startDate = startDate.split('.')
    startDate = datetime(int(startDate[2]), int(startDate[1]), int(startDate[0]))
    start_date = startDate.strftime('%d.%m.%Y')
    monta = int(input('Montako päivää: '))
    end_date = startDate + timedelta(days=monta-1)
    end_date = end_date.strftime("%d.%m.%Y")
    
    print(startDate)
    t.write(f'Ajanjakso: {start_date}-{end_date}\n')
    print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")
    paivakirja = {}
    i = 0
    while i < monta:
        endDate = startDate + timedelta(days=i)
        aika = endDate.strftime("%d.%m.%Y")
        syote = input(f"Ruutuaika {aika}: ")
        paivakirja[aika] = syote.replace(' ', '/')
        minuutit.append(syote)
        i += 1
    
    c = 0
    for m in minuutit:
        s = m.split(' ')
        x = [int(i) for i in s]
        for y in x:
            c += y
    kk = c / monta
    t.write(f'Yht. minuutteja: {c}\n')
    t.write(f'Keskim. minuutteja: {kk}\n')
    for pvm, aikaa in paivakirja.items():
        t.write(f'{pvm}: {aikaa}\n')
    print(f'Tiedot tallennettu tiedostoon {tiedosto}')