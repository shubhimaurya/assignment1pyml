import csv
filename = "data.csv"

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    print(f"Contents of {filename}:")
    for row in reader:
        print(row)
