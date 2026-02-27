#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato `dd/mm/aaaa` 
# y muestra por pantalla, el día, el mes y el año.
fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])