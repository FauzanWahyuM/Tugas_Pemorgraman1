print("----------Program Menghitung Sederhana---------------")
bil = int(input("Masukkan Angka: "))
jmlh = 0
smdgn = ""

while bil > 0:
    jmlh += bil
    smdgn += str(bil)
    if bil != 1:
        smdgn += " + "
    bil -= 1

print("Hasil: ", smdgn, "=", jmlh)
