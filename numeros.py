import csv

with open('libro1', newline='') as f:
    lector = csv.reader(f)
    for fila in lector:
        print(', '.join(fila))