matematik_not_liste = [22, 11, 54, 65, 12, 88]
turkce_not_liste = [44,55,66,77,11]
biyoloji = [11,33,55,66,77]

not_sozlugu = {"isim": "emre", "ders": "matematik", "notu": 51}

def sozluk_fonksiyonu(sozluk):

    for k,v in sozluk.items():

        #print(k, v)

        if k == "notu":

            if v > 50:

                print("geçti")



def not_hesabi(notlar):

    for n in notlar:

        if n > 50:

            print("geçti")


# Fonksiyon Çağırma

#not_hesabi(matematik_not_liste)

#not_hesabi(turkce_not_liste)

#not_hesabi(biyoloji)

#sozluk_fonksiyonu(not_sozlugu)

####################################################################

def calisan_maaslari_zam(isim, departman, ucret, oran=False):


    if oran:

        zamli_ucret = ucret * (1 + oran)

    else:

        zamli_ucret = ucret 

    mesaj = """
        Çalışan:        {}
        Departman:      {}
        Zamlı Ucret:    {}
    """.format(isim, departman, zamli_ucret)

    return mesaj

# print(calisan_maaslari_zam(departman="IT", ucret=3000, oran=0.20, isim="Emre"))

# print(calisan_maaslari_zam("ali", "IT", 2000))

########################################



# sonsuz parametreli fonlsiyon



def topla(*d):

    toplam = 0

    for i in d:

        toplam = toplam + i

    return toplam


#print(topla(23, 12, 34, 54, 11, 33, 55, 66, "65", "11", "emre", 33))


def kisi_listesi(*kisiler):

    for i in kisiler:

        print(i, " Kayıt Edildi...")


#kisi_listesi("emre", "ali", "Ayşe")

def kisi_listesi2(**kisiler2):

    for k,v in kisiler2.items():

        msj = """
        Paramerte İsmi  /   Değeri
        {}              /   {}    
        """.format(k, v)

        print(msj)

    #return msj


kisi_listesi2(isim="emre", yas=22, okul="Osmangazi")



