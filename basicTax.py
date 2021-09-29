# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Basit olarak KDV'siz ürünlerin KDV oranını hesaplar.

These codes are written using the Pycharm editor in Python.
This code does calculates the tax rate. Tax rates are based on the Turkish economy.
"""

sign = str(input("Elektronik ürünler için 1'e basınız !" + "\n" +
                 "Genel Tüketim Ürünleri için 2'ye basınız !" + "\n" +
                 "KDV indirimi uygulanan ürünler için 3'e basınız !" + "\n" + "Seçiminiz ?: "))

price = int(input("Şimdi ürün fiyatını giriniz: "))

tax1 = 0.18
tax2 = 0.08
tax3 = 0.01

if sign == "1":
    egTotal = price * tax1
    print("Vergi oranı:", egTotal)

if sign == "2":
    egTotal = price * tax2
    print("Vergi oranı:", egTotal)

if sign == "3":
    egTotal = price * tax3
    print("Vergi oranı:", egTotal)
