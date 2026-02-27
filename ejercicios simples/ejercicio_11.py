#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
#final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
#depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
#mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
#Redondear cada cantidad a dos decimales.
cuenta_ahorros= float(input("Introduce la cantidad inicial invertida: "))
intereses=0.04
balance_1=cuenta_ahorros*(1+intereses)
print("El balance del primer año sería: "+ str(round(balance_1,2)))
balance_2=balance_1*(1+intereses)
print("El balace del segundo año sería:"+ str(round(balance_2,2))) 
balance_3=balance_2*(1+intereses)
print("El balance del tercer año sería: "+str(round(balance_3,2)))