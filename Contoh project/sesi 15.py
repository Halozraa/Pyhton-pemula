import random

def operasi_bilangan(x, y, operator):
    if operator == 'perkalian':
        return x * y
    elif operator == 'pembagian':
        return x / y
    elif operator == 'pertambahan':
        return x + y
    elif operator == 'pengurangan':
        return x - y
    else:
        return "Operator tidak valid"

while True:
    # Data penampung
    angka1 = random.randint(1, 10)
    angka2 = random.randint(1, 10)

    # Memilih operasi
    print('''
Dibawah ini ada Tes soal Matematika
    1. pertambahan
    2. pengurangan
    3. perkalian
    4. Pembagian''')

    # Input dari user
    memilih = input("Mau Test yang mana: ")

    # Memilih operasi
    if memilih == "1":
        operator = 'pertambahan'
    elif memilih == "2":
        operator = 'pengurangan'
    elif memilih == "3":
        operator = 'perkalian'
    elif memilih == "4":
        operator = 'pembagian'
    else:
        print("Masukan dengan benar  di list pilihan yang ada !")
        continue

    # Menghitung hasil operasi
    hasil = operasi_bilangan(angka1, angka2, operator)

    # Menampilkan soal
    print(f"Soalnya adalah {angka1} {'+' if operator == 'pertambahan' else '-' if operator == 'pengurangan' else '*' if operator == 'perkalian' else '/'} {angka2}")

    # Jawaban user
    jawab_user = input("Jawabannya adalah: ")

    # Mengonversi jawaban user menjadi tipe data float
    try:
        jawab_user = float(jawab_user)
    except ValueError:
        print("Masukkan jawaban berupa angka!")
        continue

    # Memeriksa jawaban user
    if jawab_user == hasil:
        print("Jawaban kamu benar")
    else:
        print(f"Jawaban kamu salah, Hasilnya adalah {hasil}")

    play_again = input("Mau tetap main [y/n]: ")
    if play_again.lower() == "n":
        break
