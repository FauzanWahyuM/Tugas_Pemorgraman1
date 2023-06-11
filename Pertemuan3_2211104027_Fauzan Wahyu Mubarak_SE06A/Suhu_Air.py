suhu = int(input("Masukkan Suhu Air: "))
if (suhu < 0):
    print("Suhu", suhu, "derajat adalah Padat")
elif (suhu > 0 & suhu <100):
    print("Suhu", suhu, "derajat adalah Cair")
else: 
    print("Suhu", suhu, "derajat adalah Uap")
