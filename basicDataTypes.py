# -*- coding:utf-8 -*-
"""
Bu kodlar Python ile Pycharm editörü kullanılarak yazılmıştır.
Bu kod basit sorular topluluğudur. Sorular Türkçedir.

These codes are written using the Pycharm editor in Python.
This code it contains simple questions in Turkish,

used random.
"""



import random


def againAndAgain():
    print(
        "Kim Python veri tipi ister yarışmamıza hoş geldiniz !(Binary veri tipleri kullanılmamıştır) 11 soruya kadar cevap verebilirsiniz. Kaç Soruya Cevap Vermek İstersiniz ? :")
    numberofproblems = input()
    numberofproblems = int(numberofproblems)

    if numberofproblems > 11:
        print("Özür dileriz ancak 11 soruya cevap verebilirsiniz !")
        againAndAgain()
    if numberofproblems <= 0:
        print("Oynamadığınız için teşekkürler")
        exit(0)
    else:
        for problemswanted in range(numberofproblems):
            question1 = 1
            question2 = 2
            question3 = 3
            question4 = 4
            question5 = 5
            question6 = 6
            question7 = 7
            question8 = 8
            question9 = 9
            question10 = 10
            question11 = 11

            questionNumber = random.randint(1, 11)

            if questionNumber == 1:
                question1Answer = input("Pythonda metinsel ifadeleri tutan veri tipi nedir ?: ")
                if question1Answer == "string" \
                        or question1Answer == "String" \
                        or question1Answer == "str":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap String veri tipidir !")

            if questionNumber == 2:
                question2Answer = input("Pythonda haritalama(mapping) yapabilen veri tipi nedir ?: ")
                if question2Answer == "dict" \
                        or question2Answer == "DİCT" \
                        or question2Answer == "Dict" \
                        or question2Answer == "DICT" \
                        or question2Answer == "dict.":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Dict veri tipidir !")

            if questionNumber == 3:
                question3Answer = input("Pythonda ondalıklı sayı türünü tutan veri tipi nedir ?: ")
                if question3Answer == "Float" \
                        or question3Answer == "float" \
                        or question3Answer == "FLOAT":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Float veri tipidir !")

            if questionNumber == 4:
                question4Answer = input("Python'da tamsayı veri tipi nedir ?: ")
                if question4Answer == "int" \
                        or question4Answer == "İNT" \
                        or question4Answer == "INT" \
                        or question4Answer == "İnt" \
                        or question4Answer == "integer" \
                        or question4Answer == "INTEGER" \
                        or question4Answer == "Integer":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap int yada integer veri tipidir !")

            if questionNumber == 5:
                question5Answer = input(
                    "Python'da ileri düzey matematiksel işlemlerde kullanılan sayısal veri tipi nedir ?: ")
                if question5Answer == "Complex" \
                        or question5Answer == "COMPLEX" \
                        or question5Answer == "complex":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Complex veri tipidir !")

            if questionNumber == 6:
                question6Answer = input("Python'da değeri sadece true yada false olabilecek veri tipi nedir ?: ")
                if question6Answer == "Bool" \
                        or question6Answer == "Boolean" \
                        or question6Answer == "BOOL" \
                        or question6Answer == "BOOLEAN" \
                        or question6Answer == "bool" \
                        or question6Answer == "boolean":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Bool yada Boolean veri tipidir !")

            if questionNumber == 7:
                question7Answer = input(
                    "Herhangi bir sayıda diğer objeleri içinde bulunduran bir sandık vazifesi görebilen" + "\n" + "ve bir listede birden fazla tip öğenin yanyana bulunabildiği veri tipi nedir ?: ")
                if question7Answer == "list" \
                        or question7Answer == "LİST" \
                        or question7Answer == "List" \
                        or question7Answer == "LIST":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap List veri tipidir !")

            if questionNumber == 8:
                question8Answer = input(
                    "Sıralı ve değiştirilemez bir koleksiyon çeşidi olan, ( ) parantezler kullanılarak" + "\n" + "yazılan ve list veri tipindeki bazı metotları içermeyen veri tipi nedir ?: ")
                if question8Answer == "Tuple" \
                        or question8Answer == "TUPLE" \
                        or question8Answer == "tuple":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Tuple veri tipidir !")

            if questionNumber == 9:
                question9Answer = input(
                    "Python'da belirli aralıkta bulunan sayıları göstermek için kullanılan veri tipi nedir ?: ")
                if question9Answer == "range" \
                        or question9Answer == "RANGE" \
                        or question9Answer == "Range":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Range veri tipidir !")

            if questionNumber == 10:
                question10Answer = input(
                    "Python'da küme görevi gören ve Liste, Tuple ve Dict gibi veri tiplerini barındırabilen," + "\n" + "değiştirilebilir bir veri yapısı nedir ?: ")
                if question10Answer == "set" \
                        or question10Answer == "SET" \
                        or question10Answer == "Set":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Set veri tipidir !")

            if questionNumber == 11:
                question11Answer = input(
                    "Python'da Set veri türünün kısıtlanmış halidir. Bu veri türüne ekleme," + "\n" + "silme, değiştirme yapılamaz immutable(değiştirilemez) veri tipidir. Bu veri tipi nedir ?: ")
                if question11Answer == "frozenset" \
                        or question11Answer == "FROZENSET" \
                        or question11Answer == "Frozenset" \
                        or question11Answer == "FrozenSet":
                    print("Doğru Cevap Tebrikler !")
                else:
                    print("Malesef cevabınız doğru değil, doğru cevap Frozenset veri tipidir !")


againAndAgain()
