#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

oikea = random.randint(1,10)
arvaus = int(input("Arvaa luku1-10"))
while True:
    if arvaus == oikea:
        print("Oikein jee oikea luku oli", oikea )
        break
    elif arvaus > oikea:
        print("Suurempi")
    else:
        print("Pienempi")
