# n =int(input('n='))
# match n:
#     case 1:
#         print('Dushanba')
#     case 2:
#         print('Seshanba')
#     case 3:
#         print('Chorshanba')
#     case 4:
#         print('Payshanba')
#     case 5:
#         print('Juma')
#     case 6:
#         print('Shanba')
#     case 7:
#         print('Yakshanba')
#     case _:
#         print('not found')

# n =int(input('n='))
# match n:
#     case 1:
#         print('yomon')
#     case 2:
#         print('qoniqarsiz')
#     case 3:
#         print('qoniqarli')
#     case 4:
#         print('yaxshi')
#     case 5:
#         print('alo')
#     case _:
#         print('xato')

# oy =int(input('oy='))
# match oy:
#     case 1|12|2:
#         print('qish')
#     case 3|4|5:
#         print('bahor')
#     case 6|7|8:
#         print('yoz')
#     case 9|10|11:
#         print('kuz')
#     case _:
#         print("xato")

# oy =int(input('oy='))
# match oy:
#     case 1|3|5|7|9|12:
#         print('31 kun bor')
#     case 4|6|8|10:
#         print('30 kun bor')
#     case 2:
#         print('28 kun bor')
#     case _:
#         print("xato")

# A = float(input("A sonini kiriting: "))
# B = float(input("B sonini kiriting: "))
# amal = int(input("Amalni kiriting (1 - qo'shish, 2 - ayirish, 3 - ko'paytirish, 4 - bo'lish): "))
# match amal:
#     case 1:
#         natija = A + B
#     case 2:
#         natija = A - B
#     case 3:
#         natija = A * B
#     case 4:
#         if B == 0:
#             natija = "Xatolik: Nolga bo'lish mumkin emas."
#         else:
#             natija = A / B
#     case _:
#         natija = "Noto'g'ri amal."
#
#
# print("Natija:", natija)

# birlik= int(input("Birlik uzunligini tanlang  1-desimetr, 2-kilometr, 3-metr, 4-millimetr, 5-santimetr. "))
# uzunlik = float(input("Kesma uzunligini kiriting: "))
#
# match birlik:
#     case 1:
#         natija = uzunlik / 10
#     case 2:
#         natija = uzunlik * 1000
#     case 3:
#         natija = uzunlik
#     case 4:
#         natija = uzunlik / 1000
#     case 5:
#         natija = uzunlik / 100
#     case _:
#         natija = "Noto'g'ri birlik tanlandi"
#
#
# print(f"Kesmaning uzunligi metrlarda: {natija}")


# ogrlik_turi= int(input("Birlik uzunligini tanlang  1-kilogram, 2-milligram, 3-gramm, 4-tonna, 5-sentner. "))
# massa = float(input("Ogrilk birligini kiriting: "))
#
# match ogrlik_turi:
#     case 1:
#         natija = massa
#     case 2:
#         natija = massa / 1000000
#     case 3:
#         natija = massa / 1000
#     case 4:
#         natija = massa * 1000
#     case 5:
#         natija = massa * 100
#     case _:
#         natija = "Noto'g'ri birlik tanlandi"
#
#
# print(f"Ogrilk birligi kilogramda: {natija}")


# son = int(input("Yoshni kiriting (20-69): "))
#
# birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
# onliklar = ["", "on", "yigirma", "ottiz", "qirq", "ellik", "oltmish"]
#
# match son:
#     case son if 20 <= son <= 69:
#         on = son // 10
#         birlik = son % 10
#
#         match birlik:
#             case 0:
#                 print(onliklar[on] + " yosh")
#             case _:
#                 print(onliklar[on] + " " + birliklar[birlik] + " yosh")
#     case _:
#         print("Iltimos, 20-69 orasida son kiriting")


# son = int(input("Yoshni kiriting (20-69): "))
#
#
# birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
# onliklar = ["", "on", "yigirma", "ottiz", "qirq", "ellik", "oltmish"]
#
# match son:
#     case son if 10 <= son <= 40:
#         on = son // 10
#         birlik = son % 10
#
#         match birlik:
#             case 0:
#                 print(onliklar[on] + " ta masala")
#             case _:
#                 print(onliklar[on] + " " + birliklar[birlik] + " ta masala")
#     case _:
#         print("Iltimos, 10-40 orasida son kiriting")


# import math
#
# pi = 3.14
#
# nomi = input("Berilgan elementni kiriting (R, D, L, S): ")
# qiymat = float(input("Element qiymatini kiriting: "))
#
# match nomi:
#     case "R":
#         R = qiymat
#         D = 2 * R
#         L = 2 * pi * R
#         S = pi * R ** 2
#         print(f"Qolgan elementlar: Diametr: {D}, Uzunlik: {L}, Yuza: {S}")
#
#     case "D":
#         D = qiymat
#         R = D / 2
#         L = 2 * pi * R
#         S = pi * R ** 2
#         print(f"Qolgan elementlar: Radius: {R}, Uzunlik: {L}, Yuza: {S}")
#
#     case "L":
#         L = qiymat
#         R = L / (2 * pi)
#         D = 2 * R
#         S = pi * R ** 2
#         print(f"Qolgan elementlar: Diametr: {D}, Radius: {R}, Yuza: {S}")
#
#     case "S":
#         S = qiymat
#         R = math.sqrt(S / pi)
#         D = 2 * R
#         L = 2 * pi * R
#         print(f"Qolgan elementlar: Diametr: {D}, Uzunlik: {L}, Radius: {R}")
#
#     case _:
#         print("Xato")

import math


nomi = input("Berilgan elementni kiriting (a, c, h, S): ").lower()
qiymat = float(input("Element qiymatini kiriting: "))

match nomi:
    case "a":
        a = qiymat
        c = a * math.sqrt(2)
        h = c / 2
        S = (c * h) / 2
        print(f"Qolgan elementlar: Gipotenuza: {c}, Balandlik: {h}, Yuza: {S}")

    case "c":
        c = qiymat
        a = c / math.sqrt(2)
        h = c / 2
        S = (c * h) / 2
        print(f"Qolgan elementlar: Katet: {a}, Balandlik: {h}, Yuza: {S}")

    case "h":
        h = qiymat
        c = 2 * h
        a = c / math.sqrt(2)
        S = (c * h) / 2
        print(f"Qolgan elementlar: Katet: {a}, Gipotenuza: {c}, Yuza: {S}")

    case "s":
        S = qiymat
        c = math.sqrt(2 * S)
        h = c / 2
        a = c / math.sqrt(2)
        print(f"Qolgan elementlar: Katet: {a}, Gipotenuza: {c}, Balandlik: {h}")

    case _:
        print("Xato")
