a = "emre istanbul"

yaslar = [22, 33, 12, 55, 17, 66]


for age in yaslar:

    if age < 18:

        #print("Mekana Girmezsiniz...")
        pass

    else:
        pass
        #print("Hoşgeldiniz...")


sözlük = {"bir":1,"iki":2,"üç":33,"dört":43}
# items()
# keys()
# values()


for eleman in sözlük.values():

    if eleman > 10 and eleman < 50:

        #print("Eleman  ", eleman)
        pass



# Döngüde i değerlerini ekrana yazdırma
basinc = [22, 33, 12, 55, 66, 110]

status = True

i = 0

for b in basinc:

    if b > 60:
        print("Basınç kritik seviyede. Tank kapatılıyor....")
    
    else:
        print("Tank Çalışıyor... Basınç: {}".format(b))


# Ödev
notlar = [43, 23, 99, 71, 11, 10, 33]
durum = []


















while status:

    if basinc[i] > 60:

        #print("Basınç kritik seviyede. Tank kapatılıyor....")
        status = False
    
    else:
        #print("Tank Çalışıyor...")
        pass
    i = i + 1

print("While Döngüsü dışındayım ")





    



    


