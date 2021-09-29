# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Basitçe sizden 1 ile 10 arası bir rakam tahmin etmenizi ister.

These codes are written using the Pycharm editor in Python.
This code asks you to guess only one number from 1 to 10,

used random.
"""

import random

x = 1

while x == 1:
    number = int(input("1-10 arası bir sayı tuttum, hadi tahmin et !"))
    guessing = random.randint(1, 10)

    if number == guessing:
        print("Bildiniz !\n")
        x = int(input("Tekrar oynamak istermisiniz ? Evet için 1, Hayır için 2"))

    else:
        print("Bilemediniz !", guessing)

print("Tekrar oyna !")
