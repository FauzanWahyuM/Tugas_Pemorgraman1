def jumlah(x, y):
    rumus1 = x + y
    return rumus1

def kali(x, y):
    rumus2 = x * y 
    return rumus2

def bagi(x, y):
      if y != 0:
        return x / y
      else :
        print("Tidak bisa membagi dengan 0!")

def kurang(x, y):
    rumus4 = x - y
    return rumus4

def pangkat(x, y):
    rumus5 = x ** y
    return rumus5


while True:
            print("---------------Kalkulator---------------")
            print("1. Penjumlahan")
            print("2. Perkalian")
            print("3. Pembagian")
            print("4. Pengurangan")
            print("5. Pangkat")
            
            pilih = (input("\nMasukkan Pilihan Anda : "))
                   

            if pilih == "1":
                bil1 = (float(input("\nMasukkan Bilangan ke - 1 : ")))
                bil2 = (float(input("Masukkan Bilangan ke - 2 : ")))
                hasil1 = jumlah(bil1, bil2)
                print("\nHasil Penjumlahan : ", hasil1)
            elif pilih == "2":
                bil1 = (float(input("\nMasukkan Bilangan ke - 1 : ")))
                bil2 = (float(input("Masukkan Bilangan ke - 2 : ")))
                hasil2 = kali(bil1, bil2)
                print("\nHasil Perkalian : ", hasil2)
            elif pilih == "3":
                bil1 = (float(input("\nMasukkan Bilangan ke - 1 : ")))
                bil2 = (float(input("Masukkan Bilangan ke - 2 : ")))
                hasil3 = bagi(bil1, bil2)
                print("\nHasil Pembagian : ", hasil3)
            elif pilih == "4":
                bil1 = (float(input("\nMasukkan Bilangan ke - 1 : ")))
                bil2 = (float(input("Masukkan Bilangan ke - 2 : ")))
                hasil4 = kurang(bil1, bil2)
                print("\nHasil Pengurangan : ", hasil4)
            elif pilih == "5":
                bil1 = (float(input("\nMasukkan Bilangan ke - 1 : ")))
                bil2 = (float(input("Masukkan Bilangan ke - 2 : ")))
                hasil5 = pangkat(bil1, bil2)
                print("\nHasil Pangkat : ", hasil5)
            else:
                print("\nBilangan Anda Tidak Valid!")
                continue

            
            while True:
                terus = input("\nApakah Anda ingin melanjutkan? (iya/tidak) = ")
                if terus == "iya" or terus == "tidak":
                    break
                else:
                    print("Pilihan Anda Tidak Valid!")
        
            if terus == "tidak":
                print("Sampai jumpa dan Terima kasih!")
                break
