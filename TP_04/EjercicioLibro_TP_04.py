# Capitulo 4

#factorial = 4 * 3 * 2 * 1

#factorial = 4 * \
            # 3 * \
            # 2 * \
            # 1

# factorial = ( 4 *
#               3 *
#               2 *
#               1 )

# num = int(input("Ingrese un numero: "))
#
# if num > 0 :
#     print("El numero es mayor a zero")
#     if num % 2 == 0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")
# elif num < 0 :
#     print("El numero es negativo")
# else:
#     print("El numero es 0")
#




#valor = None

#valor = True

#if valor != None:
# if valor is None:
#     valor = int(input("Ingrese un numero: "))
# else:
#     print("Tiene algun valor")



# valor = 123
#
# if valor is not None:
#     print(valor)
#



# color = input('ingrese un color: ').lower()
#
# match color:
#     case 'verde':
#         print('color verde 🟩🟩🟩')
#     case 'azul':
#         print('color azul 🟦🟦🟦')
#     case 'rojo':
#         print('color rojo 🟥🟥🟥')
#     case _:
#         print('colo no encontrado')



# punto = (3,7,3)
#
# match punto:
#     case (x, y):
#         print('Estos puntos: '+str(punto) + ' estan en un plano (2d)')
#     case (x, y, z):
#         print('Estos puntos: '+str(punto) + ' estan en el espacio (3d)')
#     case _:
#         print('no se encontro el plano')



# auths =[
#     {'username': 'sdelquin','password':'1234'},
#     {'email':'sdelquin@gmail.com','token':'4321'},
#     {'email':'test@test.com','password':'ABCD'},
#     {'username': 'sdelquin','password':1234}
# ]
#
# for auth in auths:
#     print(auth)
#     match auth:
#         case {'username':str(username),'password':str(password)}:
#             print('autenticando con usuario y contraseña')
#             print(f'{username}: {password}')
#         case {'email':str(email),'token':str(token)}:
#             print('autenticando con email y token')
#             print(f'{email}: {token}')
#         case _:
#             print("no se pudo autenticar con ningun metodo!")
#     print('----')


