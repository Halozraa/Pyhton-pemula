# Materi cinta
list_jawab = {"1": 'Yes',
              "2": 'No',
              "3": 'I dont know'}
print(list_jawab)

# Menampilkan jawaban
for kunci, pilihan in list_jawab.items():
    print(f"{kunci}. {pilihan}")

while True: 
    try:
        pilihan = input("Apakah kamu suka aku: ")
        if pilihan in ["Yes", "No", "3"]:
            break
        else:
            print("Fack you")
    except:
        print("Terjadi kesalahan, kembali ke pertanyaan awal.")
        continue

# Eksekusi    
if pilihan == "Yes":
    print("Aku juga suka kamu!")
elif pilihan == "No":
    print("Tapi aku suka kamu!")
elif pilihan == "3":
    while True:
        try:
            pilihan = input("Kenapa kamu tidak tahu? Apakah kamu mau mencoba lagi? (ya/tidak): ")
            if pilihan.lower() == "ya":
                break
            elif pilihan.lower() == "tidak":
                break
            else:
                print("Pilihan tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")
        except:
            print("Terjadi kesalahan, kembali ke pertanyaan awal.")
            continue
else:
    print("Bisa baca gak sih")
