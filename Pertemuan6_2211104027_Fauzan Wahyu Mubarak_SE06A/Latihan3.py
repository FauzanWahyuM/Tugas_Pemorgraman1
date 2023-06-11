bil1 = (int(input("Masukkan bilangan 1 : ")))
bil2 = (int(input("Masukkan bilangan 2 : ")))

def hitung_perbandingan(bil1, bil2):
    if bil1 > bil2:
        print(bil1 , "Bilangan Lebih besar")
    elif (bil1==bil2):
        print(bil1, "sama dengan", bil2)
    else:
        print(bil2 , "Bilangan Lebih besar")

hitung_perbandingan(bil1,bil2)
