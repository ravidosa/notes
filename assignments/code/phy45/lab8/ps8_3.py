import csv

eigens = []
with open("eigen.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        eigens = row[:-1]
eigens = sorted(eigens)
print(eigens)