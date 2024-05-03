# cara memasukan data yang di luar function

anak = "ibrahim"
jago = "matematika"

def main():
    global anak,jago # ketik sintaks ini untuk memasukan dari luar func
    print(f"Halo si {anak} ,dia itu loh jago {jago}, tau gak sih ,sis.")

    while True :
        try:
            jawaban = input("tau/gak: ")
            if jawaban == "tau":
                print("Tau dong sis")
                break
            elif jawaban == "gak":
                print("gak tau sis")
                break
            else:
                print("Masukan pilihan yang benar")

        except KeyError:
            print("ketika tidak memasukan jawaban yang benar akan saya ulang programnya")

if __name__ == "__main__":
    main()
