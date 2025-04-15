
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printed_designs = []

def print_designs(designs):
    """Prints designs"""
    for desing in designs:
        print(f"Printing {desing}")
        printed_designs.append(desing)

def show_completed_designs(printed_designs):
    for design in printed_designs:
        print(f"{design} was printed")

print_designs(unprinted_designs)
show_completed_designs(printed_designs)

print(unprinted_designs)
