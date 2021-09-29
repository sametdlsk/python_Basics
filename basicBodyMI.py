# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Bu kod Vücut kitle endeksinizi hesaplar.

These codes are written using the Pycharm editor in Python.
This code Body Mass Index(BMI) calculator.
"""

name = input("Adınız nedir ?:")
weight = int(input("Kilonuzu giriniz:"))
height = float(input("Boyunuzu nokta kullanarak ondalıklı olarak giriniz:"))
calc = weight / (height * height)

print(name, "Vücut Kitle Endeksiniz:", calc)
if 0 <= calc <= 18:
    print("Zayıfsınız, biraz daha kilo almanız gerekebilir, sağlık kuruluşlarına danışın !")
elif 18 < calc <= 24:
    print("İdeal vucut indeksine sahipsiniz")
elif 24 < calc <= 26:
    print("İdeal vucut indeksinin bir kaç basamak üstündesiniz, çok az kilo vermeniz gerekebilir !")
elif 26 < calc <= 29:
    print("Fazla kilolara sahipsiniz !")
else:
    print("Obezite tehlikesi lütfen en yakın sağlık kuruluşuna danışın !")
