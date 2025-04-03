pizza = {
    'crust': 'thick',    
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"Type of crust: {pizza['crust']}")

for topping in pizza['toppings']:
    print(f'{topping.title()} added')