import time
import random
#Programa principal  
print("Bienvenido a la arena de lucha PyForce ")
time.sleep(2)
personaje = input("Elija pesonaje: \n[a]\t  Enano \n[b]\t  Caballero \n ")

# creacion de estadistica de  ataque/defensa de los personajes con random
ataque_enano=random.randint(1,12)
ataque_caballero=random.randint(1,12)
defensa_enano=random.randint(1,6)
defensa_caballero=random.randint(1,6)

#creacion de la posibilidad de ataque/defensa de cada uno
if personaje== "a":
    print("El enano ataca primero !")
    time.sleep(2)
    if ataque_enano > defensa_caballero:
        print("El enano gana !")
        print(ataque_enano)
        print(defensa_caballero)
    else:
        print("El caballero gana !")
        print(ataque_enano)
        print(defensa_caballero)

if personaje== "b":
    print("El caballero ataca primero !")
    time.sleep(2)
    if ataque_caballero > defensa_enano:
        print("El caballero gana !")
        print(ataque_caballero)
        print(defensa_enano)
    else:
        print("El enano gana !")
        print(ataque_caballero)
        print(defensa_enano)