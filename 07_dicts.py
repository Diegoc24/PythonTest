#Dicts

my_dict = {}
print(type(my_dict))

my_new_dict = dict()
print(type(my_new_dict))

my_dict = {
    "Nombre": "Diego",
    "Apellido": "Caruso",
    "Edad": 26,
    "lenguajes": {"JavaScrip", "Python", "HTML"}

}

print(my_dict["Nombre"])
print(len(my_dict))

my_dict["calle"] = "Julio A Roca"
print(my_dict)

del my_dict["calle"]
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
my_dict_values = list(my_dict.values())
print(my_dict_values)
print("Diego" in my_dict_values)

my_other_dict = dict.fromkeys(my_dict, "A value")
print(my_other_dict)

my_other_dict = dict.fromkeys(my_dict)
print(my_other_dict)