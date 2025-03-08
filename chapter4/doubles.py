
doubles = []

for value in range(0,11,2):
    doubles.append(value*2)
print(doubles)
print(f"Min: {min(doubles)}, Max: {max(doubles)}, Sum: {sum(doubles)}")

squares = [value**2 for value in range(1,11)]
print(squares)
