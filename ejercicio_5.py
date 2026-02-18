# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
horas= float (input("Dame el numero de horas trabajadas : "))
coste= float (input("Dame el coste por hora : "))

paga= horas*coste

print("Le corresponde la siguiente paga : ",paga)