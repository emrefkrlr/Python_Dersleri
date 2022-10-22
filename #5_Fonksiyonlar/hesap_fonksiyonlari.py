# toplama işleme

from io import UnsupportedOperation


def toplam(sayi1, sayi2):

    sonuc = sayi1 + sayi2

    return sonuc


def cikarma(sayi1, sayi2):

    sonuc = sayi1 - sayi2

    return -sonuc

def bölme(sayi1, sayi2):

    try:

        sonuc = sayi1 / sayi2

        return sonuc

    except ZeroDivisionError:

        print("Error: Sıfıra bölme hatası oldu. İkinci 0 olamaz.")
    
    except AttributeError:

        print("Error: Attribute error")

    except Exception as e:
        print("Error: Other error. {}".format(e))

    

    


def carpma(sayi1, sayi2):

    sonuc = sayi1 * sayi2

    return sonuc

def genel_hesap(a, b):

    return carpma(sayi1=a, sayi2=b)





def sonsuz_toplama(*args):

    try:
        
        toplam = 0
        for i in args:

            if isinstance(i, int): # Gelen veri integer mı kontorü yapar

                print("Sayı: ", i)

                toplam = toplam + i

        return toplam

    except Exception as e:
            
        print("sonsuz_toplama error: {}".format(e))


def kisi_bilgileri(**kwargs):

    try:

        for i, v in kwargs.items():

            print("""
                Başlık:     {}   
                Değer:      {}

            """.format(i, v))

        return "Bitti"

    except Exception as e:
        print("kisi_bilgileri error: {}".format(e))

