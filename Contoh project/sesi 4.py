
#pengtgunaan int dan float
angka = 10.5
integer_angka = int(angka) #Mengoversikan Menjadi integer
float_angka = float(integer_angka) #mengoversikan kembali menjadi float
print(integer_angka)
print(float_angka)

print("contoh ke dua")

nilai = 20
nilai_integer = int(nilai)
nilai_float = float(nilai)

print(integer_angka)
print(float_angka)

# User Input: Menghitung Luas Lingkaran
jari_jari = float(input("Masukan jari-jari lingkaran :"))
luas = 3.14 * jari_jari **2
print("Luas lingkarang adalah :", luas)

# Identity Operator
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) #output : false karena a dan b adalah dua objek yang berbeda
