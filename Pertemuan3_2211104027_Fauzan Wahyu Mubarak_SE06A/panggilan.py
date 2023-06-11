gender = input("Perempuan atau laki-laki ? (L/P): ")
if(gender == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ayah!")
    elif(status == 'N'):
        print("Hallo Bang!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bunda!")
    elif(status == 'N'):
        print("Hallo Neng!")
    else:
        print("Tidak ada dalam pilihan")