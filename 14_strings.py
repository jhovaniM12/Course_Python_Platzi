text = "Ella baila programando con python"
print("python" in text)
print("javascript" in text)

if "python" in text:
    print("Hola")
else:
    print("elegiste mal")

size = len("amor") #len lo que hace es contar el numero de caracteres
print(size)

#METODOS DE STRING *******************************************************
print(text)
print(text.upper()) #Pasar todo el texto a mayusculas   
print(text.lower()) #Pasar todo a minusculas
print(text.count("a")) #el metodo count cuenta cuantos caracteres hay repetidos.
print(text.swapcase()) #el metodo swapcase cualquier caracter que este en minuscula lo pasa a mayusculas y viceversa.
print(text.startswith("Ella"))#nos devolvera true o false dependiendo si el texto empieza por la primera palabra.
print(text.replace("python","JavaScript")) #con el metodo replace le indicamos que palabra que queremos que reemplace.

text_2 = "este es el segundo titulo"
print(text_2)
print(text_2.capitalize()) #con "capitalize" ponemos la primera palabra en mayusculas.
print(text_2.title()) #por cada palabra va a poner el primer caracter en mayusculas.
print(text_2.isdigit())
print("30330".isdigit())