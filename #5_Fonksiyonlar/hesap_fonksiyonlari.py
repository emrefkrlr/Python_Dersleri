# toplama işleme

def toplam(sayi1, sayi2):

    sonuc = sayi1 + sayi2

    return sonuc


def cikarma(sayi1, sayi2):

    sonuc = sayi1 - sayi2

    return -sonuc

def bölme(sayi1, sayi2):

    if sayi2 != 0:

        sonuc = sayi1 / sayi2

        return sonuc
    
    else:

        return "{} sayısı 0 a bölünemez".format(sayi1)


def carpma(sayi1, sayi2):

    sonuc = sayi1 * sayi2

    return sonuc

def genel_hesap(a, b):

    return carpma(sayi1=a, sayi2=b)