#game tebak tebakan simple

import random

# varibel
pesan = "Welcome To My Mini Games"
person_position = random.randint(1,6)
won = "Selamat kamu Menang"
loser = "Kamu Kalah idiot"

#Penyambutan
print("******************************")
print(f"***{pesan}***")
print("******************************")

#bentuk goa
bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] *6
goa = goa_kosong.copy()
goa[person_position-1]= "|0_0|"

   # #input user(User disuruh memilihi)
while True :
    print("Ada penjahat nih bersembunyi diantara goa ini")
    print(goa_kosong)
    pilihan = int(input("Ada dinomer berapa penjahatnya 1/2/3/4/5/6 :"))
    if pilihan in [1, 2, 3, 4, 5, 6]:
        break
    else :
        print("## Coba Masukan Jawaban yang Ada dipilihan itu ##")

confirm = input(f"Apakah anda yakin dengan pilihannya : {pilihan} \n Y/N :")

if confirm == "Y": 
    # Eksekusi program       
   if pilihan == person_position:
       print(f"\n{goa} \n ### {won} ###")

   else:
       print(f"\n {goa}  \n ### {loser} ###")
elif confirm == "N":
    exit
else :
    print("Error code")   

