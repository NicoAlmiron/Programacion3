#listas
#
# listaPrueba = [1,2,3,4,5,6]
#
# print(listaPrueba[2:])
#
# listaPrueba.append(7)
# print(listaPrueba)
#
# listaPrueba.insert(5,8)
# print(listaPrueba)
#
# listaPrueba.extend([9,10,11,12])
# print(listaPrueba)
#
# print(4 in listaPrueba)
#
# listaPrueba.remove(4)
# print(listaPrueba)
# print(4 in listaPrueba)
#
# listaPrueba.pop()
# print(listaPrueba)
#
# listaPrueba.sort()
# print(listaPrueba)
#
# listaPrueba.reverse()
# print(listaPrueba)
#
# listaPrueba.clear()
# print(listaPrueba)

# Tuplas

tuplaPrueba = (1,2,3,4,5,6)

print(tuplaPrueba)

print(tuplaPrueba[2])
mlista = list(tuplaPrueba)

print(mlista)

miTupla = tuple(mlista)

print(miTupla.count(5))

print(len(miTupla))


otraTupla = ('nicolas', 7,4,2000)

nombre, dia, mes, anio = otraTupla

print(nombre, str(dia), str(mes), str(anio))

otra2datupla = miTupla + otraTupla
print(otra2datupla)

