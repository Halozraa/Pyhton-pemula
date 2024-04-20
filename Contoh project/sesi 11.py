dico = 750000
diskon = 0.10
harga = 500000
if harga < dico:
    total_harga = dico - (dico * diskon)
    print("Total harga setelah diskon:", total_harga)
else:
    print("Error")
