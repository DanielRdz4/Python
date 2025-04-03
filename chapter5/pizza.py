
toppings_requested=[]
toppings_available =['peperoni','onions','chili','cheese','pineapple']

for i in range(3):
    topping = input("Which toppings would you like?: ").lower()
    toppings_requested.append(topping)

for i in range(3):
    if toppings_requested[i] in toppings_available:
        print(f"Adding {toppings_requested[i]}")
    else:
        print(f"{toppings_requested[i]} is not available")