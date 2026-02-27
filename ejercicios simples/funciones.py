def saludo():
    print("hola que tal")

def potencia_diez(numero):
    resultado=numero**10
    print(resultado)

def potencia_libre(numero,potencia):
    resultado=numero ** potencia 
    print(resultado)

def potencia_libre2(numero,potencia):
    resultado=numero ** potencia 
    return resultado


# ejercicio 1 : crea una funcion  que imprima la raiz cuadrada de un 
# numero que le pases por argumento 
def raiz_cuadrada(numero):
    resultado= numero ** 0.5
    print (resultado)

#ejercicio 2 : crea una funcion que imprima la media d dos numeros que le passes 
def media(numero_1,numero_2):
    media=(numero_1+numero_2)/2
    print(media)

# Ejercico 3 : funcion que me dice el ahorro  mensual que consigo
def ahorro (presu,luz,agua,internet,alquiler,comida, ocio):
    gastos=luz+agua+internet+alquiler+comida+ocio
    ahorro=presu-gastos
    print (ahorro)

#ejecucion del códio para hacer las funciones básica 
potencia_diez(2)
potencia_libre(2,3)
valor=potencia_libre2(2,3)
resultado_final=valor+ 5
print(resultado_final)
raiz_cuadrada(4)
media(20,80)
ahorro(1500,80,50,50,600,500,200)