def insertionasc_sort(array):
        for i in range (1, len(array)):
            item = array [i]
            j = i - 1 

            while j >= 0 and array[j] > item:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = item 
            

def insertiondsc_sort(array):
        for i in range (1, len(array)):
            item = array [i]
            j = i - 1 

            while j >= 0 and array[j] < item:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = item 
            
        
def tambah_buku(array):
    total_buku = int(input("Masukkan Total Buku : "))
    n = 1
    while total_buku > 0:
        nama_buku = input(f"Masukkan judul buku ke- {n} : ")
        array.append(nama_buku)
        n += 1
        total_buku -= 1

def urut_sort(buku):
    print("\n=========== Urutkan?============")
    print("1. Sorting Ascending")
    print("2. Sorting Descending")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        insertionasc_sort(buku)
        print("\nDaftar buku setelah diurutkan secara ascending:")
        
    elif pilihan == '2':
        insertiondsc_sort(buku)
        print("\nDaftar buku setelah diurutkan secara descending:")
        
    else:
        print("Pilihan tidak valid")

def cetak_hasil(array):
    print(" ")
    for i, n in enumerate(array):
        print(f"Judul buku ke- {i+1} : {n}")

data_buku = []
tambah_buku(data_buku)
urut_sort(data_buku)
cetak_hasil(data_buku)



