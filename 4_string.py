Name = input("Cual es tu nombre?")
LastName = input("Cual es tu apellido?")
Age = input("Cual es tu edad?")

FullName = Name + " " + LastName

print(FullName)

quote = "I'm Nicolas"

print(quote)

Template = "Hola mi nombre es " + Name + "y mi apellido es: " + LastName
print(Template)

Template = "Hola mi nombre es {} y mi apellido es {}, tengo {} años".format(Name,LastName,Age)
print(Template)
