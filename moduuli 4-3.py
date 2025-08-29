#ohjelma kysyy lukuja siihen saakka että annetaan tyhjä jono
#sen jälkeen ohjelma tulostaa saaduista luvuista pienimmän ja suurimman

luvut= []
while True:
    luku = input("Anna lukuja:")
    if (luku== ""):
        print("Virheellinen luku")
        break

    else:
        luku = int(luku)
        luvut.append(luku)

print("Tässä isoin ja pienin luku:")
print(max(luvut))
print(min(luvut))