matakuliah = (int(input("\nMasukkan Jumlah Mata Kuliah : ")))
print()
nilai1 = []

for i in range(int(matakuliah)):
    nilai = (int(input("Masukkan Nilai Mata Kuliah ke - {} = ". format(i+1))))
    nilai1.append(nilai)

total = sum(nilai1)
rata = total/len(nilai1)

if 100 >= rata >= 90:
    predikat = 'A'
elif rata >= 70:
    predikat = 'B'
elif rata >= 50:
    predikat = 'C'
elif rata >= 30:
    predikat = 'D'
else:
    predikat = 'E'

if any(nilai > 100 for nilai in nilai1):
    print("\nNilai yang anda masukkan tidak valid!")
else:
    print("\nHasil Predikat {} dengan nilai : ".format(predikat), rata)
    for i, n in enumerate(nilai1):
        print("Mata kuliah ke-{}    : {}".format(i+1, n))
