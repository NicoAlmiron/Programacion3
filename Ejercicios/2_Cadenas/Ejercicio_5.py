# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase
# invertida.

frase = input("Ingrese una frase: ")

#solucion
#fraseInvertida = frase[::-1]

fraseInvertida = ""
revertidor = reversed(frase)
for _ in frase:
    fraseInvertida += next(revertidor) # utiliza next para moverse por el arreglo

print(fraseInvertida)


#https://realpython.com/reverse-string-python/