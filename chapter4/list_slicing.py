#prinero se usa un slice para copiar la lista completa, y se guarda en otra variable, creando dos listas iguales pero independientes
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append('hotdog')
friends_food.insert(0,'ham')

#Se imprimen las listas a las que se les agregaron datos, demostrando que son dos listas distintas

print(my_foods)
print(friends_food)

#si se iguala la lista my_foods = firends_food, entonces tienes una sola la lista "my_foods" cualquier cambio que se haga desde ella o firends_food, afectará a ambas.

friends_food = my_foods

print(my_foods)
print(friends_food)

friends_food.pop(3)

print(my_foods)