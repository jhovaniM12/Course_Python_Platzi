name = "Nicolas"
print(type(name))

name = 12
print(type(name))

age = 12
print("Mi edad es: " + str(age))

age = int(input("Escribe tu edad: ")) #Cuando ingresamos un valor en input siempre nos devuelve una str o string.
age += 5
age = int(age)
print(f"Tu edad en 5 años sera de: {age}")
print(type(age))
print(f"La edad es:{age}") #Esta es tambien una forma de hacer transformaciones.

print("Hola", age)