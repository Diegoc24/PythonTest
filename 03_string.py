#strings

my_string = "my string"
my_other_string = 'my other string'

#cantidad de caranteres de los diferentes strings

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

#saltos de linea de strings
new_line_string = "my string \nmy other string"
print(new_line_string)

#tabulador de strings
new_tab_string = "my string... \t run string"
print(new_tab_string)

#anular caracteres especiales
new_force = "my\\n stryng \\t other string" 
print(new_force)

#diferentes tipos de formateo de strings

name, surname, age = "Diego", "caruso", 26

value = f"my name is {name} {surname} and i am {age} years old"
print(value)
value_two = "my name is %s %s and i am %d years old" % (name, surname, age)
print(value_two)
value_three = "mi nombre es {} {} y tengo {}".format(name, surname, age)
print(value_three.capitalize()) #capitalize solo pone la primer letra en mayúscula
value_four = "Mi nombre es " + name + " " + surname + " y tengo " + str(age)
print(value_four)

#desestructurando un string en variables

a, b, c, d, e, f, g, h, i = "francisco"

print(a)
print(d)
print(i)

nombre = a + b + c + d + e + f + g + h + i

print(nombre)

#slicing de strings
print("slicing")
print(nombre[2:5])
print(nombre[2:])
print(nombre[:5])
print(nombre[0:9:2])
print(nombre[-3])

#revertir strings
reversed_string = nombre[::-1]
print(reversed_string)

#funciones de strings

print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
print(nombre.count("c"))
print(nombre.isnumeric())
print("3".isnumeric())
print(nombre.upper().islower())
print(nombre.startswith("fr")) #comprueba si empieza con fr




