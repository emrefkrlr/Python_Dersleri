## Değişken Tanımı ve Veri Tipleri

name = "Emre" # String (str)
age = 21 # Integer (int)
ortalama = 4.44 # Float (float)
status = False # Boolen (boolen) True


print(age - 43)



## Veri Yapıları
# 1 - Liste
manav_listesi = ['emre', 'fikirlier', 23, 23.1, 'istanbul', True, "asd", 22, """23"""]
# Python listelerde liste sırası (index) 0' dan başlar

print(manav_listesi[1])

print(manav_listesi[8])

liste_icinde_liste = [
    "emre", 
    [21, 43, 23 ,0, 11, "istanbul", True, ["turkiye", "ankara"]],
    ["python", "php", 22],
    "fikirlier"
    ]

# listeye erişmek
print(liste_icinde_liste[1][7][1])

# liste elemanlarını değiştirmek
liste_icinde_liste[1][6] = 99999999999999
print(liste_icinde_liste)

# listeye aşağıdaki eleman ekleyemiyoruz
liste_icinde_liste[4] = "Bardak"
print(liste_icinde_liste)


# 2 - Tupple (demet)
manav = ("elma", 16, True, 2.1)

print(manav)
print(manav[0])

# Tupple eleman değitrimeye izin vermez
manav[0] = "armut"
print(manav)

# 3 - Sözlükler

kisi_listesi = {
    "isim": "Emre",
    "soyisim": "Fikirlier",
    "sehir": "Istanbul",
    "yas": 28,
    "status": True,
    "oran": 12.1,
    "programla_diller": ["python", "php"]
}

# Sözlük elemanlarına erişmek
print(kisi_listesi["isim"])

print(kisi_listesi["sehir"])

print(kisi_listesi["programla_diller"][1])


# Sözlük de eleman değiştirme
kisi_listesi["sehir"] = "Kayseri"

print(kisi_listesi["sehir"])

kisi_listesi["yas"] = "30"

print(kisi_listesi["yas"])


# Sözlük de yeni eleman eklemek
kisi_listesi["ücret"] = 1000
print(kisi_listesi)
print(kisi_listesi["ücret"])


# LEN Fonksiyonu

print(len("emre fikirlier"))
isim = "emre fikirlier"

print(isim[5])


# Type Fonksiyonu

name = "Emre" 
age = 21 
ortalama = 4.44
status = False
liste = [12, 23, 43]

print(type(kisi_listesi))