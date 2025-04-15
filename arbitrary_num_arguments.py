
def print_pizza_recipe(size, *toppings):
    print(f"\nPizza size: {size}")
    print(f"Pizza toppings:")
    for topping in toppings:
        print(f"- {topping}")

print_pizza_recipe(26, 'cheese','salami')
print_pizza_recipe(28, 'chili')