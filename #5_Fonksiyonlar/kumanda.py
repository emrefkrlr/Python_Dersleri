

def on_of(click):

    if click:

        status = True
        print("Televizyon Açıldı....")
    
    else:
        status = False
        print("Televizyon Kapatıldı....")

    return status

def channel_list():

    channels = ["TRT", "ATV", "Show", "KanalD", "Fox", "TLC"]

    return channels


def change_channel(number=False, up=False, down=False):

    channels = channel_list()
    # Kanal Numarası verdiğinde
    channels_lenght = len(channels)

    if number:

        

        if number > channels_lenght or number < 0:

            print("Kanal bulunamadı.")

        else:

            return channels[number]

    else:

        now_channel_index = 0

        if up:

            if now_channel_index < channels_lenght:
                now_channel_index = now_channel_index + 1
            else:

                print("Kanal bulunamadı ")

            return channels[now_channel_index]


        if down:

            if now_channel_index > 0:
                
                now_channel_index = now_channel_index - 1
            
            else:

                print("Kanal bulunamadı ")

            return channels[now_channel_index]

        print("Kanal Numarası bulunamadı")
        return channels[now_channel_index]






# TV Aç
on_of(True)
# Kanal Değiştirecek numara ile
print(change_channel())
# Kanal Değiştirecek numara ok tuşu yukarı bastı
print(change_channel(up=True))
# Ses Açsın
# Kanal Değiştirsin
# Sesi Kapatsın (mute)
# Sesi Azaltsın
# TV Kapatsın
