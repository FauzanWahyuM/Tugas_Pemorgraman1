print ("--------FPB--------")

def hitung_fpb(x, y):

    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i ==0)):
            fpb = i
    return fpb
nilai = int(input("Masukkan Angka Pertama: "))
nilai2 = int(input("Masukkan Angka Kedua: "))
print("FPB = ", hitung_fpb(nilai, nilai2))