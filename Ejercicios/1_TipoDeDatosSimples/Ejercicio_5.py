# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después
# debe mostrar por pantalla la paga que le corresponde.

horas = int(input('ingrese las horas trabajadas \nhoras: '))
coste = int(input('ingrese el coste de la hora de trabajo \ncoste: '))

pago = horas * coste

print('el pago por ' + str(horas) + 'hs trabajadas es de: ' + str(pago))