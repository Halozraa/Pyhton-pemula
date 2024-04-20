# Menghitung Bunga

print('''
      Calculator Simple menghitung Bunga pinjaman
      ===== ****** =====
      ''')
pinjam = float(input("Masukan Jumlah pinjaman anda :"))
bulan = float(input("Berapa bulan anda mau meminjam :"))
bunga = 0.05
hasil = (pinjam / bulan)* bunga
konversi1 = int(hasil)

print("Bunga tiap bulannya adalah",konversi1)
hasil1 = pinjam + hasil
konversi2 = int(hasil1)
print("jadi yang harus anda bayar sebesar", konversi2)