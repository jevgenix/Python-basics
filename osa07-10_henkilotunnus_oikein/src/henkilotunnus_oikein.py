from datetime import datetime
from string import digits

def onko_validi(hetu: str):
    if len(hetu) != 11:
        return False
    
    numerot = hetu[7:10]
    for x in numerot:
        if x not in digits:
            return False

    pv = hetu[0:2]
    kk = hetu[2:4]
    vali = hetu[6]
    if '+' in vali:
        vuosi = '18' + hetu[4:6]
    elif '-' in vali:
        vuosi = '19' + hetu[4:6]
    elif 'A' in vali:
        vuosi = '20' + hetu[4:6]
    else:
        return False

    try:
        syntynyt = datetime(int(vuosi), int(kk), int(pv))
    except:
        return False
    
    mjono = list('0123456789ABCDEFHJKLMNPRSTUVWXY')
    arvo = hetu[0:6] + hetu[7:10]
    index = int(arvo)%31
    if hetu[10] != mjono[index]:
        return False        
    
    return True
    

if __name__ == '__main__':
    print(onko_validi('310827-906F'))
    print(onko_validi('131052-308T'))
