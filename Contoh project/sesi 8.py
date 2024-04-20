# menghitung kecepatan jarak dan waktu
print("# Create by nagi #")
def kecepatan(a, b):
    return a/b

def jarak(a, b):
    return a*b

def waktu(a, b):
    return a/b

# ambil data
print("Selamat datang dikalkulator")
print("Pilih operasi:")
print("1. kecepatan")
print("2. jarak")
print("3. waktu")

pilihan = input("Masukan pilihan (1/2/3):")
# Lakukan operasi yang diminta
if pilihan == '1':
    angka1 = float(input("Masukkan Jaraknya: "))
    angka2 = float(input("Masukkan Waktu: "))
    print("Kecepatnya Adalah : ",kecepatan(angka1, angka2))
elif pilihan == '2':
    angka1 = float(input("Masukkan Kecepatan: "))
    angka2 = float(input("Masukkan waktu: "))
    print("Jaraknya Adalah : ",jarak(angka1, angka2))
elif pilihan == '3':
    angka1 = float(input("Masukkan Jarak: "))
    angka2 = float(input("Masukkan Kecepatan: "))
    print("Waktu yang dibutuhkannya : ",waktu(angka1, angka2))
else :
    print("Erorr code")
    
