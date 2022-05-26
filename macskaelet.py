import random

eletek_szama = 9

szavak = ['pizza', 'rózsa', 'málna', 'fagyi', 'mókus', 'mappa']

titkos_szo = random.choice(szavak)

ismeretlen_szo = list('?????')

szivecske = u'\u2764'

kitalalta = False


def fedd_fel(betu, titkos_szo, ismeretlen_szo):
    index = 0
    while index < len(titkos_szo):
        if betu == titkos_szo[index]:
            ismeretlen_szo[index] = betu
        index = index + 1


while eletek_szama > 0:
    print(ismeretlen_szo)
    print('Életek: ' + szivecske * eletek_szama)
    valasz = input('Találgass betűt vagy az egész szót: ')

    if valasz == titkos_szo:
        kitalalta

    if valasz in titkos_szo:
        fedd_fel(valasz, titkos_szo, ismeretlen_szo)

    else:
        print('Helytelen. Elvesztesz egy életet')
        eletek_szama = eletek_szama - 1

if kitalalta:
    print('Nyertél! A titkos szó ' + titkos_szo + ' volt')
else:
    print('Vesztettél! A titkos szó ' + titkos_szo + ' volt')