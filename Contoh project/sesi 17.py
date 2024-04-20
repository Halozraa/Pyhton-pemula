import sys
from io import StringIO

def datas_style():
    datas = [
        ('Nama', 'Pemasukan', 'Pengeluaran'),
        ('Budi', 1000000, 500000),
        ('Hasan', 1000000, 350000),
        ('Ibnu', 1000000, 300000),
    ]

    garis = "-" * 35
    print(garis)
    for delta in datas:
        print('|', end='')
        for item in delta:
            print(f"{item:<10}|", end="")  # Menambahkan spasi ke kanan untuk membuat kolom
        print()  # Pindah ke baris baru setelah satu baris data selesai dicetak
        if delta[0] == 'Nama':
            print(garis)
        else:
            print("-" * 35)  # Mencetak garis mendatar sebagai baris bawah selain baris nama
    print(garis)
    
    sys.stdout = sys.__stdout__
    
    return datas  # Mengembalikan nilai datas





welcome = '''dibawah ini sudah ada data yang tersimpan

1.Data View
2.Editor Data
'''
welcome1 = '''Data mana yang mau anda ubah: 

1.Pemasukan Budi
2.Pengeluaran Budi
3.Pemasukan Hasan
4.Pengeluaran Hasan
5.Pemasukan Ibnu
6.Pengeluaran ibnu
'''

print(welcome)
pilihan = int(input("Masukan Pilihanmu: "))

if pilihan == 1:
    datas_style()
elif pilihan == 2:
    datas_copy = tuple(datas_style())
    print(welcome1)
    pilihan1 = int(input("Masukan Pilihanmu: "))
    if pilihan1 == 1:
        ubah = int(input("Masukan Pemasukan budi"))
        datas_copy[1][1]= ubah
        print(datas_copy)
else:
    pass