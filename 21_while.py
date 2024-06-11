"""
counter = 0

while counter < 10:
    counter += 1
    print(counter)

#Una iteracion es una repeticion.

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break #con break rompemos un ciclo de manera forzada.
    print(counter)
"""
counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)


"""
El continue sirve para saltarse ciertas partes del código. 
Por ejemplo, si quiero hacer un conteo de números hasta el 10,
pero no quiero que el 5 sea contado, hago lo siguiente:

number = 0
while number < 10:
  number += 1
  if number == 5:
    continue
  print(number)
"""