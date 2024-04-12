# Rumus menghitung Diskon

print("****Calculator simple mengitung Diskon barang**** ")
print("### Anda berhasil mendapatkan diskon sebesar 40% ###")

harga_barang = float(input("Masukan harga awalnya :"))
Harga = 0.40 * harga_barang
konversi1 = int(Harga)
print("Anda Sekarang bisa menghemat :",konversi1)
diskon = harga_barang - konversi1
konversi2 = int(diskon)
print("sekarang anda hanya perlu membayar sebesar :",konversi2)