import csv

lists = []

with open("odais/asobiba.csv") as f:
    for row in csv.reader(f):
        lists.append(row)


with open("odais/d-kan.csv") as f:
    for row in csv.reader(f):
        lists.append(row)

with open("odais/netaboke.csv") as f:
    for row in csv.reader(f):
        lists.append(row)
