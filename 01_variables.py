#Variables

#variable string
variable_string = "my string"
print(variable_string)

#variable boolean

variable_bolean = True
print(variable_bolean)

#variable integer

variable_integer = 5
print(variable_integer)

#variable float

variable_float = 1.5
print(variable_float)

#variable complex

variable_complex = 1j + 2
print(variable_complex)

#concatenacion de variables
print(variable_string, variable_bolean, variable_integer, variable_float, variable_complex)
print("Este es el valor de la variable string: " + variable_string)

#funcion len
print(len(variable_string))

#Variables en una linea
name, surname, age, country = "Diego", "Caruso", 26, "Argentina"
print(country, surname, age, name)

#Entrada de datos
name = input("Cual es su nombre? ")
surname = input("Cual es su apellido? ")
age = input("Cual es su edad? ")
country = input("En cual pais vive? ")
print("Su nombre y apellido es ", name, surname, "su edad es", age, "y vive en", country)

#Print agradecimiento
print("Gracias por ingresar los datos solicitados")

#No forzamos el tipo, solo sirve de reseña para otros desarrolladores
name: str = "Diego"
name = 24
print(name)
print(type(name))






