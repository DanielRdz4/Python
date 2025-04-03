rivers = {'nile': 'egypt','ramos':'allende','santa catarina':'monterrey'}

for river, city in rivers.items():
    print(f"The {river} river runs through {city}")

for river in rivers.keys():
    print(river)

for city in rivers.values():
    print(city)