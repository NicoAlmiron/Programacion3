# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro co
# rreo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


correo = input('ingrese su correo: ')

correoNuevo = correo.split('@')[0] + "@ceu.es"

print('su nuevo correo es: ', correoNuevo)