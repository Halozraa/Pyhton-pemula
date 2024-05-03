import time

print("Aku suka kucing loh,apa kamu juga suka?\ny or n")

while True :
    try:
        answer = input("Apa jawabnmu: ")
        if answer == 'y':
            print("ya aku juga suka")
            break
        elif answer == 'n':
           for a in range (10):
               answer1 = "Padahal kucing itu menggemaskan"
               time.sleep(0.5)
               print(answer1)
               
        else:
            print("Harus Menjawab dengan benar!!!")
    except :
        print("xxxx")