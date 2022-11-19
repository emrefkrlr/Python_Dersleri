girdi = int(input("bir sayı girin "))

sonuc = 1
for i in range(1, girdi + 1):

    sonuc *= i

print(girdi, "sayının faktoriyeli ", sonuc)