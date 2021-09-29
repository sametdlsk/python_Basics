# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Sizin için basit anlamda NickName oluşturur.

These codes are written using the Pycharm editor in Python.
This code crate a nickname for u, combination is firstname
1. and 2. letters +
lastname 1. and 2. +
favourite color first 1. 2. and the last and the previous one
"""

print("Sizin için nickname yaratır, Lütfen sorulara cevap veriniz !")
firstname = input("İsminiz nedir ?")
lastname = input("Soyisminiz nedir ?")
likecolor = input("En sevdiğiniz renk nedir ?")
newNick = firstname[0] + firstname[1] + lastname[-2] + lastname[-1] + likecolor[0] + likecolor[1] + likecolor[-2] + \
          likecolor[-1]

print(newNick)
