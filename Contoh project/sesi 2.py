nilai_ujian = [80, 75, 90, 85, 88]
nilai_ujian.append(95)
nilai_ujian.remove(75)
print(nilai_ujian)

#Dictionary
biodata = {"nama":"andi", "umur": 25, "kota":"Jakarta"}
print(biodata["nama"])

#Operasi Aritmatika:
x = 5
y = 10
hasil = x + y
print(hasil)

#Operasi Perbandingan
a = 10
b = 5
print(a>b) #output(jawabannya pasti true kalau benar)

# Percabangan (Conditional Statements): 
nilai = 85
if nilai >= 80:
    print("Nilai Anda A")
elif nilai >= 70:
    print("Nilai Anda B")
else:
    print("Nilai Anda C")
    
# Pengulangan (Loops):
for i in range(5):
    print(i)
    
while nilai < 7:
    nilai += 1
    print(nilai)
    
    #fungsi
def tambah(a, b):
    return a + b

print(tambah(5, 3))

