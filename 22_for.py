"""
for elemet in range(1, 21): #Con range le estamos dando el conjunto de iteraciones.
    print(elemet)
"""
my_list = [23, 34, 45, 19]
for elemt in my_list:
    print(elemt)

my_tuple = ('Nico', 'Daniel', 'Jhovani')

for element in my_tuple:
    print(element)

my_dict = {
    'name': "Camisa",
    'price': 100,
    'stock': 89
}
for key in my_dict:
    print( key, '=>' ,my_dict[key])

for key, value in my_dict.items():
    print(key, "=>", value)

people = [
    {
        'name': 'Carlos',
        'age': 20,
        'lenguage': 'Spanish'
    },
    {
        'name': 'Jhovani',
        'age': 23,
        'lenaguage': 'English'
    }
]

for person in people:
    print('name =>',person['name'])

#En un for podemos iterar bajo un conjuto de datos, puede ser una lista , sea un rango o un diccionario,
# a diferencia que en el ciclo while hay una condicion que ejecuta el ciclo

"""
La variable element suele llamarse en referencia a lo que se está recorriendo y es donde se almacena dinamicamente elemento por elemento.

Si trabajamos con una lista de gatitos podrían llegar a ver


for gato in gatos:
	print(gato)
Donde se está iterando en la lista gatos y en cada iteración se almacena nuestro valor en la variable gato que se denota como singular.
"""
contador = 0
while contador < 5:
    contador += 1
    print(contador)

