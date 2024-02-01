# sets

my_set = set()
print(type(my_set))
my_set = {"JavaScript"}
my_other_set = {} #Estando vacio, el tipo de dato es un dict
print(type(my_other_set))

my_other_set = {"diego", "caruso", "emanuel", 26, 1.63} 
print(my_other_set) #Cuando imprimimos en pantalla se puede ver que no es ordenado

#my_other_set[2] No se permite sustraer los valores como en las listas o en las tuplas 

my_other_set.add("azul") #Se pueden agregar valores, pero no de una manera ordenada
print(my_other_set)

my_other_set.add("azul") #Los set no repiten los valores
print(my_other_set)

#De esta forma podemos comprobar si los valores existen

print("diego" in my_other_set)
print("juan" in my_other_set)

#De esta forma se pueden borrar determinados valores
my_other_set.remove("azul")
print(my_other_set)

#Se pueden re asignar valores al set
my_set = {"javascript", "Python", "Node"}
print(my_set)

#De esta manera se pueden concatenar los valores
my_other_set = my_other_set.union(my_set)
print(my_other_set)

#Se pueden eliminar valores repetidos en otro set
my_other_set = my_other_set.difference(my_set)
print(my_other_set)

#Se puede eliminar el contenido del set con clear()
my_other_set.clear()
print(my_other_set)

#Se puede eliminar por completo el set con del
del my_other_set


