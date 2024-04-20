# Definisikan fungsi-fungsi operasi matematika
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol"

# Ambil masukan dari pengguna
print("Selamat datang di Kalkulator Sederhana")
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Lakukan operasi yang diminta
if pilihan == '1':
    print("Hasil penjumlahan:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")
