# total_purchase = float(input("Masukkan nilai total belanja: "))

# if total_purchase > 150000:
#     discount = total_purchase * 0.2
#     discounted_purchase = total_purchase - discount
#     print("Nilai belanja setelah diskon: Rp", discounted_purchase)
# else:
#     print("Nilai belanja tanpa diskon: Rp", total_purchase)

# a = float(input("Masukkan panjang sisi a: "))
# b = float(input("Masukkan panjang sisi b: "))
# c = float(input("Masukkan panjang sisi c: "))

# # Urutkan sisi-sisi segitiga
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b

# # Cek jenis segitiga menggunakan rumus Pythagoras
# a_squared = a ** 2
# b_squared = b ** 2
# c_squared = c ** 2

# if a_squared + b_squared == c_squared:
#     print("Segitiga siku-siku")
# elif a_squared + b_squared < c_squared:
#     print("Segitiga tumpul")
# else:
#     print("Segitiga lancip")

a = int(input("Masukkan bilangan bulat a: "))
b = int(input("Masukkan bilangan bulat b: "))
c = int(input("Masukkan bilangan bulat c: "))

temp = 0

if a < b:
    temp = a
    a = b
    b = temp

if b < c:
    temp = b
    b = c
    c = temp

if a < b:
    temp = a
    a = b
    b = temp

print("Bilangan urut dari terbesar ke terkecil: ", a, b, c)
