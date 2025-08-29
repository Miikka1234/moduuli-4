#Ohjelma joka muuttaa tuumat senttimetreiksi niin kauna kunnes annetaan negatiivinen tuumaluku
# 1 tuuma 2.54cm
while True:
    tuumat = float(input("anna tuumat: "))
    if tuumat < 0:
        print("ohjelma loppu")
        break

    cm = tuumat * 2.54
    print(cm)




