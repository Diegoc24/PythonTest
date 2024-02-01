#lists

my_list = list()
print(type(my_list))

my_list = [34,21,56,43,78,53,21,56,33,43,12,87]
print(my_list)

my_other_list = ["diego", "caruso", 26, 1.63, "Potrero"]
print(my_other_list)

print(my_other_list[0])
print(my_other_list[3])
print(my_other_list[-1])
print(my_other_list[-2])

#desestructurando la lista
name, surname, age, height, city = my_other_list
print(surname)

name, surname, age, height, city = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3], my_other_list[4]
print(height)

#concatenacion de listas

my_new_list = my_list + my_other_list
print(my_new_list)

#multiplicacion de listas

my_new_list = my_other_list * 3
print(my_new_list)

#funciones de listas
my_other_list.append("Azul") #agrega un elemento al ultimo
print(my_other_list)

my_other_list.remove("Azul") #remueve un elemento especifico
print(my_other_list)

my_new_list = my_other_list.pop() #remueve el ultimo elemento y lo guarda en una variable si es necesario
print(my_new_list)
print(my_other_list)

my_list.pop(2) #remueve un elemento en una posicion especifica
print(my_list)

my_other_list.insert(5, "Potrero") #inserta un elemento en una posicion especifica
print(my_other_list)

my_list.sort() #ordena la lista de menor a mayor
print(my_list)

print(my_list.count(43))  #cuenta la cantidad de veces que aparece un elemento

my_list.reverse() #Da vuelta los valores de la lista
print(my_list)

my_list.clear() #Elimina todos los elementos de la lista
print(my_list)

del my_other_list #Elimina la lista

