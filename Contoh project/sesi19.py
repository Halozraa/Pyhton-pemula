balance = 100000 # = 100.000


while True:
    try:
        num = float(input("Deposit: ")) #float itu adalah angka desimal hampir sama dengan integer sama-sama angka
        break #jika memasukan data yang benar looping akan berhenti dan program bakalan berjalan
    except ValueError:
        print("Masukan angka Bukan huruf")


balance += num # untuk menjumlahkan dengan sisa saldo + Deposit
balance_rapih = (f"{balance:,}") # untuk merapihkan angka agar ada ,
print(f"Balance {balance_rapih}") # untuk menampilkan diterminal