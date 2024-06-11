"""
My_name = "Jhovani"
my_age = 23
print("Hola " + My_name)
print("El señor " + My_name, "tiene", my_age, "años")
"""


My_name = input("¿Cual es tu nombre?")
my_age = input("¿Cual es tu edad?")

print("El señor " + My_name, "tiene", my_age, "años")

#Especificar el tipo de datos de una variable.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Obtener el tipo de dato de una variable
x = 5
y = "John"
print(type(x))
print(type(y))