




#age = int(input("Yaşınızı girin: "))
age = 22

if age < 18:

    print("Mekana Girmezsiniz...")

else:

    print("Hoşgeldiniz...")


# note = int(input("X dersinden aldığınız notu girin:   "))
note = 22

if note < 0 or note > 100:

    print("Bu notu kullanamazsınız...")

elif note >= 0 and note < 50:

    print("Kaldınız..")

elif note >= 50 and note < 80:

    print("Şartlı geçtiniz.")

else:

    print("Geçtiniz")



# Sistemde kayıtlı
user_name = "emre.istanbul"
password = "emre123"

# Kullanıcıdan gelen
get_user_name = input("Kullanıcı adınız :   ")
get_pasword = input("Şifreniz:  ")

# Kullanıcının sisteme girişini kontrol ediyoruz
if get_user_name == user_name and get_pasword == password:

    print("Hoşgeldiniz...")

else:

    print("Girdiğiniz bilgiler yanlış...")




# 4 İşlem yapabilen bir hesap makinesi kodlayalım.

