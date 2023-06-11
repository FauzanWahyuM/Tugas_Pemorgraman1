#function
bil = (int(input("Masukkan Bilangan = ")))

def ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return("Bilangan yang anda inputkan adalah Genap")
    else:
        return("Bilangan yang anda inputkan adalah Ganjil")

print(ganjil_genap(bil))

#prosedur
bil = (int(input("Masukkan Bilangan = ")))

def ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        print(bil, "adalah Bilangan Genap")
    else:
        print(bil, "adalah Bilangan Ganjil")

ganjil_genap(bil)