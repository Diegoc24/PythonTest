#tuples

my_tuple = tuple()
print(type(my_tuple))
my_tuple = (14, 18, 34,21, 18)
print(type(my_tuple))

my_other_tuple = ("diego", "caruso", 26, 1.63)

print(my_other_tuple[1])
print(my_tuple[-1])

print(my_tuple.count(18))

print(my_other_tuple.index("caruso"))

#No se pueden modificar los valores internos, pero si se pueden concatenar
my_concat_tuple = my_tuple + my_other_tuple 
print(my_concat_tuple)

#Se puede modificar unicamente si convertimos la tupla en lista
my_other_tuple = list(my_other_tuple)
print(type(my_other_tuple))

my_other_tuple.insert(2, "azul")
print(my_other_tuple)

#Paso de nuevo a tupla
my_other_tuple = tuple(my_other_tuple)
print(type(my_other_tuple))

print(my_other_tuple)

#No se pueden modificar los valores internos de las tuplas, pero si se puede eliminar la tupla
del my_other_tuple

