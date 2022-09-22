# 1. Çöüzmü

List = [12,22,31,12,'emre', 42, 'python', 98, "mert", "ali"]

print(List[7])

print(len(List))

print(type(len(List)))

print(len(List) - 1)

print(List[len(List) - 1])


# 2. Çözüm

# append methodu listelerde kullanılır ve son elemana ekleme yapar

kullanicilar = [12,22,31,12,'emre', 42, 'python', 98, "mert", "ali"]
kullanicilar_1 = [12,22,31,12,'emre', 42, 'python', 98, "Emre", "ali"]
kullanicilar_2 = [12,22,31,12,'emre', 42, 'python', 98, "Farık", "ali"]

kullanicilar_2.append(44)

kullanicilar_2 = kullanicilar_2 + ["Mehmet", "18", 44]

print(kullanicilar_2)


# pop methodu bu metot da bir listeden öğe silmemizi sağlar

print(kullanicilar_2.pop())
print(kullanicilar_2)

print(kullanicilar_2.pop(3))
print(kullanicilar_2)


# sort methodu sıralama işlemi yapıyor.

uyeler = ['Mahmut', 'Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Zeynep']

print(uyeler)

print(" Sıralanmış Hali : ")

uyeler.sort()
print(uyeler)

print(" Tersten Sıralanmış Hali : ")

uyeler.sort(reverse=True)
print(uyeler)


# 3. Çözüm

dizi = [
	[0, 22, 11, 'ali'],
	['emre', 43, 'mehhmet', 11],
	[13, 'python', 32, 54, ["istanbul", "üsküdar"]]
]

print(dizi[2][4][1])

