# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corpo
# ral y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc>
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = int(input('digite su peso (Kg): '))
altura = float(input('digite su altura (Mts): '))

IMC = peso / (altura ** 2)

print('Tu indice de masa corporal es '+str(IMC))
