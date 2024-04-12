data_diri ={"Nama":"Abdul ghofur",
            "Kelas":"5 Sd",
            "Agama":"Islam"}
try :
    print(f"Nama saya adalah :{data_diri['Nama']}")
    print(f"saya kelas  :{data_diri['Kelas']}")
except KeyError:
    print("Key/nilai list tidak ditemukan")
except TypeError:
    print("Anda tidak dapat membagi/Mengkali dengan nilai string")    
else:
    print("Selamat program anda berjalan")
finally:
    print("Akhirnya Tugas saya selesai")