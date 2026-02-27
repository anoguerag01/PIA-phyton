# mensaje de binvenida 
print("Bienvenido a la calculadora virtual avanzada .A continuación elija dos numeros  " \
"y la operacion a reallizar")
#pedimos los numeros 
numero_1= input ("EScriba el primer numero: ")
numero_2= input ("EScriba el segundo numero: ")
operacion= input ("EScriba la operacion a realizar +,-,*,/ :  ")

#tranformamos numeros de cadena de texto en int

numero_1 = int(numero_1)
numero_2 = int(numero_2)

# Realizamos las operaciones segun el signo elegido
if operacion == "+":
    suma = numero_1+numero_2
    print("El resultado de la suma es {suma}")

if operacion == "-":
    resta = numero_1 -numero_2
    print("El resultado de la resta es {resta}")

if operacion == "*":
    multiplicacion= numero_1*numero_2
    multiplicacion= int(multiplicacion)
    print("El resultado de la multiplicacion es {multiplicacion}")

if operacion == "/":
    division =numero_1/numero_2
    division=int(division)
    print("El resultado de la division es {division}")