import random

# Fungsi untuk menghasilkan angka acak
def roll():
    return random.randint(1, 6)

# Meminta input jumlah pemain
while True:
    player_input = input("Berapa pemain yang ingin berpartisipasi (2-4): ")
    if player_input.isdigit():
        player_count = int(player_input)
        if 2 <= player_count <= 4:
            break
        else:
            print("Harus angka 2-4!!!")
    else:
        print("Salah, coba lagi.")

# Inisialisasi variabel
max_score = 30
player_scores = [0 for _ in range(player_count)]

# Main loop
current_player = 0
game_over = False

while not game_over:
    print(f"\nPlayer {current_player + 1}: Program sudah berjalan")

    current_score = 0  # Reset current_score di awal giliran pemain
    
    # Tanyakan apakah pemain ingin bermain
    should_roll = input("Apakah kamu ingin bermain (y)? ").lower()

    while should_roll == "y":
        value = roll()
        print(f"Kamu mengocok dadu dan mendapatkan angka {value}.")

        if value == 1:
            print("Kamu mendapat angka 1, giliranmu berakhir.")
            current_score = 0  # Mengatur current_score ke 0
            break
        else:
            current_score += value
            print(f"Skor sementara: {current_score}")

        # Tanyakan lagi apakah pemain ingin bermain
        should_roll = input("Apakah kamu ingin bermain lagi (y)? ").lower()
    
    # Tambahkan current_score ke player_scores[current_player]
    player_scores[current_player] += current_score
    print(f"Total skor kamu adalah {player_scores[current_player]}.")

    # Periksa apakah pemain telah mencapai atau melebihi max_score
    if player_scores[current_player] >= max_score:
        print(f"\nSelamat! Player {current_player + 1} memenangkan permainan dengan skor {player_scores[current_player]}!")
        game_over = True
    else:
        # Lanjutkan ke pemain berikutnya
        current_player = (current_player + 1) % player_count


'''
BELAJAR PAKAI BANTUAN CHATGPI MALAH JADI ERROR COK, DAH LAH NYERAH GUE
EHH ENGGAK DING TERNYATA HARUS KLIK ENTER SETIAP KALI PLAYER MELAKUKAN ROLL
JADI JALAN JIR
MASIH RADA ERROR SIH TAPI ,KENAPA SETIAP SESUDAH PEMAIN ROLL, HARUS KLIK ENTER DULU BARU BISA BERGANTI KE PLAYER 2 DSB.
'''