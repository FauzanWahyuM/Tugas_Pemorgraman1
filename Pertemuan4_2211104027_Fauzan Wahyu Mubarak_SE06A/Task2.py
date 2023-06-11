print("---------------Program Menghitung Pangkat--------------")

b = int(input("Masukkan bilangan: "))
c = int(input("Masukkan pencacah: "))
hp = 1

for i in range(c):
    hp *= b

print("Hasil pangkat adalah =", hp)
