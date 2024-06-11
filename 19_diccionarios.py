# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

#LAS LISTAS Y LOS DICCIONARIOS SON MUTABLES EN PYTHON.

my_dict = {
    'avion':"avion de avianca",
    'name':"Nicolas",
    'last_name':"Moreno",
    'age': 30
}
print(type(my_dict))
print(my_dict)
print(len(my_dict))
print(my_dict['age'])#Nos devuelve el valor que tenga la llave age.
print(my_dict.get('ager')) #Si no estamos seguros de la llave del diccionario podemos usar el metodo .get (con .get prevengo un error.)
print('avion' in my_dict)

"""
El siguiente paso a las listas y tuplas que vimos en anteriores, son los diccionarios.
 Y un diccionario en Python, es como un diccionario en la vida del día a día.

Es decir, cada palabra tiene asociado un significado.

Pues exactamente igual tenemos en Python, cada palabra, que llamaremos clave, tiene asociado un significado, que llamaremos valor. 
Es decir, que un diccionario no es mas que un conjunto de parejas clave – valor. 
Los diccionarios en Python son un tipo de dato realmente muy potente.
"""