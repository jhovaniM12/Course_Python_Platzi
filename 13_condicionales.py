#Los if siempre se ejecutan bajo un condicion booleana.
if True:
    print("deberia ejecutarse")

if False:
    print("Nunca se ejecuta")
"""
pet = input("¿Cual es tu mascota favorita? ")

if pet == "Perro":
    print("Tienes un buen gusto")

elif pet == "Gato":
    print("No tienes un buen gusto")
elif pet == "Pez":
    print("eres lo maximo")

else:
    print("No tienes nunguna mascota")
"""



"""
stock = int(input("Digita el stock: "))
if stock >= 100 and stock <= 1000:
    print("El estock es correcto")
else:
    print("El stock es incorrecto")

"""

numero = int(input("Ingresa un numero: "))

if numero % 2 == 0:
    print("Es un numero par")

else:
    print("Es un numero impar")