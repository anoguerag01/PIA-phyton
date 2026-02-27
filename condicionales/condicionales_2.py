#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
palabra= "contraseña"
contraseña= input("Introduce la contraseña: ")
if palabra== contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")