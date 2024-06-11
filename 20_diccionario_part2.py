person = {
    'name':"Molina",
    'last_name': "Moreno",
    'langs': ['python', 'JavaScript'],
    'age': 24
}

print(person)
person['name'] = "Jhovani"
person['age'] -= 1
person['langs'].append('Java')
print(person)

del person['last_name'] #Asi tambien podemos eliminar un elemento de la lista.
person.pop('age') #Con el metodo pop tambien podemos eliminar un elemento de la lista.
#Nota en las listas podemos correr un pop sin necesidad del argumento.
print(person)

print("Items")
print(person.items())
print("Keys")
print(person.keys())
print("Values")
print(person.values())