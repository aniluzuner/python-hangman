import random
import os

durumlar = [
    "_______\n",
    "   | \n",
    "   O \n",
    "  /",
    "|",
    "\ \n",
    "   | \n",
    "  /",
    " \ \n"
]

def adamciz(hak):
    for i in range(0,9 - hak):
        print(durumlar[i], end="")
    
def menu(kelime):
    print("Kelime: " + kelime)
    print("1 - Tekrar Oyna")
    print("Q - Çıkış")
    secim = input("Seçim: ")
    
    if secim == "1":
        oyna()
    
    if secim == "q" or secim == "Q":
        exit()


def oyna():
    kelimeler = ["MERHABA", "DÜNYA", "ARMUT", "TÜRKİYE", "KARPUZ", "YAZILIM", "ARABA", "BİLGİSAYAR"]
    kelime = random.choice(kelimeler)
    joker = 1
    hak = 8

    gozukenkelime = []

    for i in range(len(kelime)):
        gozukenkelime.append("-")


    while 1:
        os.system("cls")
        
        print("Kalan Hakkınız:", hak)
        
        adamciz(hak)
        
        if hak == 0:
            print("Kazanamadınız!")
            menu(kelime)
        
        
        if "".join(gozukenkelime) == kelime:
            print("Kazandınız!")
            menu(kelime)

        else:
            print("\n\nKelime: " + "".join(gozukenkelime))
            
            girilenharf = input("Harf Giriniz: ").replace("i","İ").upper()

            if girilenharf == "JOKER":
                if joker > 0:
                    joker = 0
                    rastgelejoker = random.randint(0, len(kelime)-1)

                for index, karakter in enumerate(kelime):
                    if index == rastgelejoker:
                        gozukenkelime[index] = kelime[index]
                else:
                    print("Joker Hakkınız Bitti.")
                
            else:
                for index, karakter in enumerate(kelime):
                    if girilenharf == kelime[index]:
                        gozukenkelime[index] = girilenharf
                    
                if girilenharf not in kelime:
                    hak -= 1

oyna()
          