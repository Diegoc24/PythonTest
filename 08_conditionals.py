#conditionals

my_condition = True

if my_condition:
    print("Se ejecuta con true en el caso de cumplir la condición")

if not my_condition:
    print("Se ejecuta si es false")
    print("Si existe el tabulado, se ejecuta, si no, se corta ejecución")


elif my_condition:
    print("Es True")

my_other_condition = 15

if my_other_condition > 10 and my_other_condition < 20: 
    print("La condición es mayor que 10 y menor que 20")

#elif en el caso que se ejecute la primer condicion, ya elif queda sin efecto, se soluciona agregando if solamente
    
elif my_other_condition == 15:
    print("La condición es 15")

if my_other_condition == 15:
    print("La condición es 15")

#En caso que una determinado variable no tenga contenido, te arroja un false incumpliendo la condición
my_variable = {20}

if my_variable: 
    print("La variable tiene contenido")

elif not my_variable:
    print("La variable no tiene contenido")