#CRUD - Create, Read, Update and Delete

numbers = [1, 2, 3, 4, 5]
numbers[-1] = 10
print(numbers) #I can update list

numbers.append(700) #con el metodo .append podemos añadir un nuevo elemento a la lista
print(numbers)

numbers.insert(0, 'Hola') #Con el metodo insert podemos añadir un elemento a la lista indicandole la posicion que va a tener.
print(numbers)

task = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + task #Asi podemos funcionar una lista, en una lista podemos tener diferentes tipos de datos.
print(new_list)

index = new_list.index('todo 2') #Asi podemos averiguar la posicion de un elemento dentro de una lista.
new_list[index] = 'todo change'
print(new_list)

new_list.remove('todo 1')
new_list.remove(700)
new_list.pop() #Este metodo elimina el ultimo elemento dentro de una lista, Nota: si no le damos ningun parametro el siempre eliminara el ultimo elemento.
new_list.pop(0) #Aqui eliminamos el primer elemento, indicando la posicion.
new_list.reverse() #Este metodo cambia de orden las posiciones de los elementos en reversa
print(new_list)

numbers_a = [1, 5, 6, 7, 3, 2] 
numbers_a.sort() #Ordenamos un elemento dentro de la lista
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort() #Va a ordenar la lista de acuerdo al abecedario.
print(strings)

#PUNTO A TENER EN CUENTA: El metodo sort no puede ordenar elementos mezclados.
"""
++Métodos de las listas++

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

"""