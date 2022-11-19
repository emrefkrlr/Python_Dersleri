
toplam = 0
satatus = True

while satatus:

    girdi = input("Bir sayı giriniz. / Çıkmak için q harhine basın:   ")

    if girdi == "q":

        satatus = False
    
    else:

        toplam = toplam + int(girdi)

print("girdiğiniz sayıların toplamı:  ", toplam)










