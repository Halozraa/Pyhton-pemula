import random

dadu = random.randint(1,2)
while True:
    try:
        player = int(input("Masukan angka: "))
        if player == True :
            break
        else:
            print("Masukan angka: ")
    except ValueError:
        print("zzzz")

if player == dadu :
    print("You win")
else:
    print("You lose")

