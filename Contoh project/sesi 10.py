# Definisikan fungsi-fungsi untuk menghitung luas
def segitiga(tinggi, alas):
    return 0.5 * tinggi * alas

def persegi_panjang(panjang, lebar):
    return panjang * lebar

def lingkaran(jari_jari):
    return 3.14 * jari_jari**2

def persegi(sisi1, sisi2):
    return sisi1 * sisi2

# List jawab
list_jawab = [
    "1. Menghitung Luas Segitiga",
    "2. Menghitung Luas Persegi Panjang",
    "3. Menghitung Luas Lingkaran",
    "4. Menghitung Luas Persegi Panjang"
]

# Menampilkan jawab
print("Jawab:")
for pilihan in list_jawab:
    print(pilihan)

while True:
    pilihan = input("Masukan pilihanmu : ")
    if pilihan in ["1", "2", "3", "4"]:
        break
    else:
        print("Manusia babi cepet jawab oyyy")

# Eksekusi jawab
if pilihan == "1":
    angka1 = float(input("Masukan Tinggi: "))
    angka2 = float(input("Masukan Alas: "))
    hasil = segitiga(angka1, angka2)
    print("Luas Segitiga adalah:", hasil)

elif pilihan == "2":
    angka1 = float(input("Masukan Panjang: "))
    angka2 = float(input("Masukan Lebar: "))
    hasil = persegi_panjang(angka1, angka2)
    print("Luas Persegi Panjang adalah:", hasil)

elif pilihan == "3":
    angka1 = float(input("Masukan Jari-jari: "))
    hasil = lingkaran(angka1)
    print("Luas Lingkaran adalah:", hasil)

elif pilihan == "4":
    angka1 = float(input("Masukan Panjang Sisi: "))
    angka2 = float(input("Masukan Panjang Sisi: "))
    hasil = persegi(angka1, angka2)
    print("Luas Persegi adalah:", hasil)

else:
    print("Jawab tidak valid.")
