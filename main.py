# 1
from datetime import datetime

def salomlashuv():
    hozir = datetime.now(12).hour

    if 6 <= hozir < 12:
        print("xayrli tong")
    elif 12 <= hozir < 18:
        print("xayrli kun")
    elif 18 <= hozir < 24:
        print("xayrli kech")
    else:
        print("xayrli tun")

salomlashuv()

# 2- masala
def hisob():
    sonlar = [10, 20, 30]
    yigindi = sum(sonlar)

    kopaytma = 1
    for i in sonlar:
        kopaytma *= i

    print(f'Yigindi: {yigindi}, Kopaytma: {kopaytma}')

hisob()

# 3 - masala
def teskari_son():
    for i in range(10, 1, -1):
        print(i)

teskari_son()


# 4
def persnl_salom(ism, til):
    if til == 'uz':
        print(f'Salom, {ism}')
    elif til == 'en':
        print(f'Hello, {ism}')
    elif til == 'ru':
        print(f'privet, {ism}')
    else:
        print('unday til qolat quvatlanmauydi')

print(persnl_salom('ali', 'privet'))


def kvadra_ryht(roy):
    for son in roy:
        print(f'{son} kvadrati = {son ** 2}')



