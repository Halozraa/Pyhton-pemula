
# # Raise Exception (Mengangkat Pengecualian)
umur = -5
if umur < 0 :
    raise ValueError("umur tidak boleh negatif")

# # Assertion
nilai = 70
assert nilai >= 0, "Nilai tidak boleh negatif"

# Try & Except (Coba & Tangkap):
try :
    angka = int(input("Masukan angka:"))
    hasil = 10 / angka
    print("Hasil pembagian adalah :",hasil)
except ZeroDivisionError:
    print("Tidak bisa membagi oleh nol!")
except ValueError :
    print("Input harus berupa angka")
    
    # Else & Finally
try :
    angka = int(input("Masukkan angka:"))
    hasil = 10/angka
except ZeroDivisionError :
    print("Tidak bisa membagi oleh nol!")
else: 
    print("Hasil pembagian adalah: ",hasil)
finally :
    print("program selesai")