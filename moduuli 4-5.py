username = input("Anna käyttäjätunnus: ")
password = input("Anna salasana:       ")
kerrat = 5
laskuri = 0
while laskuri < kerrat:
        if username == "python" and password == "rules":
            print("Tervetuloa!")
            break
        laskuri += 1
else:
    print("Pääsy evätty.")