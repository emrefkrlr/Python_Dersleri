from fonksiyonlar import *


# fonksiyona parametre ekleme

def selamla(isim, soyisim, yas):


    print(" Selam ", isim, soyisim, yas)



#selamla("Ali", "fkasfas", 123)


def topla(sayi1, sayi2):

    toplam = sayi1 + sayi2

    return toplam


def cikarma(sayi1, sayi2):

    cikarma = sayi1 - sayi2

    return cikarma


i = input("Hesap Makinesi (+,-) İşlem seç ")
a = int(input("1. sayıyı girin "))
b = int(input("2. sayıyı girin "))

if i == "+":

    print(topla(a,b))

else:

    print(cikarma(a,b))


#yeni_kayit("emre", "fikirlier", 22)


#ikinci_fonksiyon("İkinci fonk")