import csv
import os
import os.path
import itertools
import random
import sys

names = set()
files = sorted([f for f in os.listdir('data') if f.endswith('.txt')])
top_n = int(sys.argv[1])


for datafile in files:
    datafile = os.path.join('data', datafile)

    with open(datafile, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=('name', 'gender', 'count'))

        count = 0
        for row in reader:

            if row['gender'] == 'M':
                continue

            name = row['name'].title()

            if name in names:
                continue

            count += 1
            names.add(name)

            if count >= top_n:
                break

names = sorted(list(names))

for name in names:
    print name
