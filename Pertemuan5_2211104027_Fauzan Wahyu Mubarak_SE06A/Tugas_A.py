kata = (int(input("Masukkan jumlah kata: ")))
kata1 = []

for i in range(kata):
    kata2 = (str(input("Masukkan Kata = ")))
    kata1.append(kata2)


cari = (input("\nMasukkan Kata yang ingin anda cari = "))
if cari in kata1:
    indeks = kata1.index(cari)
    print(cari, "ditemukan pada indeks ke - ", format(indeks))
else:
    print("Tidak ada kata yang anda cari")
