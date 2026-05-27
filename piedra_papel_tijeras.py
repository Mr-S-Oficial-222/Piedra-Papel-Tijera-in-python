import random
import time

obj=["piedra","papel","tijeras"]

print("bienvenido a piedra papel tijera en python")

while True:
    var = input("elige piedra,papel o tijeras: ")
    if var not in obj:
        print("opcion no valida")
        continue
    com = random.choice(obj)
    print(f"la computadora eligio {com} :")
    if var == com:
        print("empate")
    elif(var == "piedra" and com == "tijeras") or \
        (var == "papel" and com == "piedra") or \
        (var == "tijeras" and com == "papel"):
        print("Ganaste")
    else:
        print("perdiste")

    con = input("¿Quieres Seguir Jugando? y/n| ")
    if con == "n":
        print("saliendo..")
        time.sleep(0.5)
        break
