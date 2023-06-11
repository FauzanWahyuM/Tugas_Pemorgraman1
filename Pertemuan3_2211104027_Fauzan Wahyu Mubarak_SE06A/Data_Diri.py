print("--------INPUT--------")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
status = input("Anda sudah menikah atau belum? (Y/N): ")
if(status == 'Y'):
    status = "Sudah Menikah"
elif(status == 'N'):
    status = "Belum Manikah"
else:
    status = "Tidak ada dalam pilihan"
agama = int(input("Agama: "))
#1=Islam, 2=Kristen, 3=Katolik, 4=Hindu, 5=Budha, 6=konghucu
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Kristen"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
elif(agama==6):
    agama = "Konghucu"
else:
    agama = "Agama tidak ditemukan"
print("------------OUTPUT------------")
print("Nama: ",nama)
print("Jenis Kelamin: ",jk)
print("Status: ",status)
print("Agama: ",agama)
