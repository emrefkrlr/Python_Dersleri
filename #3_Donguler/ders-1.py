ust_limit_sayisi = int(input("Bir sayı giriniz:  ")) # 5

toplam = 0                                      # toplam 0 
for i in range(1,ust_limit_sayisi):             # 1 den 5 e kadar olan sayılar donüyor.
    print("Döngü sayısı -> ", i)                # 1, 2, 3, 4
    
    toplam = toplam + i                         # toplam = 10

print("Girmiş olduğunuz sayıya kadar olan toplam ", toplam) # 10 
    