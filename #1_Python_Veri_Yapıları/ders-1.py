## Değişken Tanımı

name = "Emre"
age = 21
STATUS = 1

## Sayısal Değişkenler İnt Float

a = 5
print(type(a))

b = 5.1
print(type(b))

c = "5"
print(type(c))


## String İfadeler

# String Indeksleme ve Parçalama

name = "Emre Fikirlier"
#print(name[0])
#print(name[:3])
#print(name[:3], "...")

# len

print("KARAKTER SAYISINI VER")
print(len(name))

print("Değişken Tipi")
print(type(name))

# format Kullanımı





## Listeler

# İndex Kavramı
a = ["emre", "fikirlier", 30]


print(a[2])

print("KARAKTER SAYISINI VER")
print(len(a))

liste = [ 
    [1,2,3,4,5],
	['emre', 'fikirlier', 2, "3", 4],
	[]
]

print("Değişken Tipi")
print(type(a))

#urunler = ["Beypazari", "FASDF123_asd", 22.3, "Yeil"]

print(liste[1])

print(liste[1][2])

# Değişken Değiştirmek

print(a[1])
a[1] = "Mehmet"
print(a[1])




## Tupple (Demet)

b = ("emre", "fikirlier")
print("KARAKTER SAYISINI VER")
print(len(b))

# İndex Kavramı

print("------TUPLE-------")

print(b)

print(b[0])

print("Değişken Tipi")
print(type(b))

# Değişken Değiştirmek

#b[0] = "ali"
#print(b)



## Dictionary (Sözlük)

c = {

    "urun_adi" : "Beypazarı Soda",
    "fiyat": 1.25,
    "sise_rengi": "Yeşil"

}

# Eleman Erişimi

print(c["sise_rengi"])
print(c["urun_adi"], c["sise_rengi"], c["fiyat"])


# Elaman Ekleme

c["sise_etiketi"] = "TR12_fsA"
print(c)

# Eleman Değerini Değiştirme
c["fiyat"] = 2.23
print(c)


# Temel Sözlük Metodları
print(c.keys())
print(c.values())
print(c.items())


print("KARAKTER SAYISINI VER")
print(len(c))

print("Değişken Tipi")
print(type(c))



