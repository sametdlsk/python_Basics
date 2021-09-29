# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Bu kod basit metin dosyası okuyucusudur.

These codes are written using the Pycharm editor in Python.
This code basic txt reader,

used keyboard library.
"""

import keyboard

xname = input("Dosya yolunu giriniz, Daha sonra büyük harf ile yazdırmak için B tuşuna, Küçük harfle yazdırmak için K tuşuna basınız :")
xopener = open(xname)
words = xopener.read()
upperwords = words.upper()
lowerwords = words.lower()

while True:
    if keyboard.is_pressed('b'):
        print("\n", upperwords)
        break
    if keyboard.is_pressed('k'):
        print("\n", lowerwords)
        break
