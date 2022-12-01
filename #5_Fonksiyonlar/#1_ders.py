# Fonksiyon tanımı

def selamla():

    print("Fonksiyon çağrıldı")


# Fonksiyon çağırma
#print("Fonsiyon yok")
#selamla()



def cift_sayilar():

    for i in range(1,101):

        if i % 2 == 0:

            print(i)


#cift_sayilar()
#selamla()


def now_year():

    return 2022


def hesapla(dy):

    yil = now_year()

    return yil - dy


print(hesapla(1990))






























