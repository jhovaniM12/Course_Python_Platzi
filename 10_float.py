x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
y_str = format(y, "2g") #Con 2g le indicamos que solo tenga 2 digitos.
print(type(y_str))
print(y_str)
print(y_str == str(x))

tolerancia = 0.00001
print(abs(x - y) < tolerancia)

prueba = round(y,1) #La funcion round se utiliza para redondear un numero decimal
print(x == prueba)

