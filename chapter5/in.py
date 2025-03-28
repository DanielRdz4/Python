
wanted_topping = input("What topping do ypu want?:").lower()

toppings = ['mushrooms', 'onions', 'pineapple']

if wanted_topping in toppings:
    print("Available")
else:
    print("Not available")