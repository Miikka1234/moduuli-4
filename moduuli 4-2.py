#Ohjelma joka muuttaa tuumat senttimetreiksi niin kauna kunnes annetaan negatiivinen tuumaluku
# 1 tuuma 2.54cm
tuumat = float(input("Anna tuumat :"))
sentit = tuumat*2.54
if tuumat <= 0:
    print("Ohjelma loppu.")

i=1
if tuumat >= 1:
    print(sentit,"cm")
    i+=1




