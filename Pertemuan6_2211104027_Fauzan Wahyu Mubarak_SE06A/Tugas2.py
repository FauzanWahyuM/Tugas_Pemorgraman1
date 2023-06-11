#function
r1 = float(input("Masukkan Jari - Jari : "))

def luas_lingkaran1(r):
    hasil1 = 3.14 * r1 * r1
    return hasil1
print("Luas Lingakaran = ", luas_lingkaran1(r1))

def keliling_lingakaran1(r):
    hasil1 = 2 * 3.14 * r1
    return hasil1
print("Keliling Lingkaran = ", keliling_lingakaran1(r1))

#prosedur
r = float(input("\nMasukkan jari-jari: "))

def luas_lingkaran(r):
    hasil = 3.14 * r * r
    print("Luas lingkaran: ", hasil)

luas_lingkaran(r)

def keliling_lingkaran(r):
    hasil = 2 * 3.14 * r  
    print("Keliling lingkaran: ", hasil)

keliling_lingkaran(r)
