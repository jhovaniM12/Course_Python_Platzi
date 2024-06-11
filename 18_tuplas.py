numbers = (1, 2, 3, 4, 5)
strings = ('Jorge', 'Daniel','Jhovani',"Jorge") #Las tuplas se identifican por usar parentesis
print(numbers)
print(type(numbers))
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])

#NOTA: Las tuplas pueden tener diferentes tipos de datos.
#LAS TUPLAS NO SE PUEDEN MODIFICAR COMO LO HACEN LAS LISTAS, ES DECIR NO SON MUTABLES.
#Las tuplas son solo de lecturas.

print(strings.index('Jorge'))
print(strings.count('Jorge')) #Con este metodo podemos saber cuantas veces esta un elemento dentro de la tupla.

#No podemos mutar una tupla pero si podemos hacer transformaciones:

my_list = list(strings)
print(type(my_list))
print(my_list)

my_list[0] = 'Maria'
print(my_list)

convert = tuple(my_list)
print(convert)

"""
DOCUEMENTACION:

Tuplas
Estructura de datos inmutables que contiene una secuencia ordenada de elementos

Tupla = (1, 2, 3, 4)

Los elementos están separados por espacios luego de las comas
Puede contener cualquier tipo de datos
Cada posición de la tupla tiene un índice
Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
Acceder a un elemento
Tupla = (”A”, “B”, “C”)

Tupla [0] Indice a consultar

“A” Nos retorna el resultado de la posición 0 en la tupla

Encontrar un elemento
Tupla = (”A”, “B”, “C”)

“A” in Tupla

True

“Z” in Tupla

False

Metodos
Buscar el Indice de un elemento

Tupla = (”A”, “B”, “C”)

Tupla.index(”A”)

0 Nos devuelve el indice del elemento que buscamos

Numero de veces que un elemento aparece en la Tupla

Tupla = (”A”, “B”, “C”)

Tupla.count(elemento)

Tupla.count(”B”)

1 Retorna el numero de veces del elemento en la Tupla
"""