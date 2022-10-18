# Fonksyion Tanımlama
def fonksiyon_ismi():


    print("emre")


#fonksiyon_ismi() # Fonsiyon Çağrıldı


def selamla():

    print("Merhaba python dersi başlıyor")


#selamla()


def yeni_kayit(isim, soyisim, yas):

    print("Yeni Kullanıcı Tanımlandı")
    print("isim: ", isim)
    print("soyisim: ", soyisim)
    print("yas: ", yas)

# Parametrelerin Kullanımı
# 1. kullanım
#yeni_kayit("emre", "fikirlier", "30")

# 2. kullanım
#yeni_kayit(isim="emre", soyisim="fikirlier", yas=30)


def kullanicidan_bilgi_al():

    isim = input("Adınız:  ")
    print(isim)

#kullanicidan_bilgi_al()

# Default(varsayılan) değer vermek
def yeni_kayit(isim, soyisim, yas=False):

    print("Yeni Kullanıcı Tanımlandı")
    print("isim: ", isim)
    print("soyisim: ", soyisim)
    
    if yas:
        print("yas: ", yas)

#yeni_kayit("emre", "fikirlier", 22)


a = 21

def toplama(a, b):

    sonuc = a + b

    return sonuc


#print(toplama(22,11) / 300   )


def selamla():

    return "Merhaba python dersi başlıyor {}"

#print(selamla().format("emre"))

notlar = [22, 33, 12, 55, 17, 66]

# def not_kontrol(notlar):

#     for i in notlar:

#         if i > 50:

#             return "Geçti"
        
#         else:

#             return "Kaldı"

notlar = [22, 33, 12, 55, 17, 66]

def not_kontrol(n):

    if n > 50:

        return "Geçti"

    else:

        return "Kaldı"

for i in notlar:
    print(not_kontrol(i))
















